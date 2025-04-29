import tkinter as tk
from outils_canva.constantes import TAILLE_POINT, COULEUR_POINT, ZOOM_IN_FACTOR, ZOOM_OUT_FACTOR, COULEUR_ARETE, CANVAS_HAUTEUR, CANVAS_LARGEUR, SCROLLX1, SCROLLX2, SCROLLY1, SCROLLY2
import outils_canva.geometrie as geo
from outils_canva import geometrie as fm

# Variables globales
canva = None
sommets = []
point_deplace = None
label_compteur = None
label_facteur_zoom = None
facteur_global = 1.0
derniere_pos_souris = None

callbacks = {
    "reset": None,
    "is_connected": None,
    "get_parametres": None,
    "set_parametres": None,
    "get_type_graphe": None,
}

def set_canvas(canvas):
    global canva
    canva = canvas

def enregistrer_callback(nom, fonction):
    if nom in callbacks:
        callbacks[nom] = fonction
    else:
        raise ValueError(f"Nom de callback inconnu : {nom}")

def set_label_compteur(label):
    global label_compteur
    label_compteur = label
    update_label_compteur()

def set_label_zoom(label):
    global label_facteur_zoom
    label_facteur_zoom = label
    update_label_zoom()

def update_label_zoom():
    if label_facteur_zoom:
        label_facteur_zoom.config(text=f"Zoom : x{facteur_global:.2f}")

def update_label_compteur():
    if label_compteur and canva:
        nb_sommets = len(sommets)
        nb_aretes = 0
        for i in range(len(sommets)):
            for j in range(i + 1, len(sommets)):
                if callbacks.get("is_connected") and callbacks["is_connected"](sommets[i], sommets[j]):
                    nb_aretes += 1
        label_compteur.config(text=f"Sommets : {nb_sommets} | Arêtes : {nb_aretes}")

def reset_callbacks():
    for key in callbacks.keys():
        callbacks[key] = None

def reset():
    global sommets, label_compteur, label_facteur_zoom, facteur_global, canva, derniere_pos_souris, point_deplace

    sommets.clear()

    if canva is not None:
        try:
            canva.delete("all")
            canva.xview_moveto(0.5)
            canva.yview_moveto(0.5)
        except tk.TclError:
            pass

    if label_compteur is not None:
        try:
            label_compteur.config(text="Sommets : 0 | Arêtes : 0")
        except tk.TclError:
            label_compteur = None 

    if label_facteur_zoom is not None:
        try:
            label_facteur_zoom.config(text="Zoom : x1.00")
        except tk.TclError:
            label_facteur_zoom = None

    facteur_global = 1.0
    derniere_pos_souris = None
    point_deplace = None

    if callbacks.get("reset"):
        callbacks["reset"]()

def appliquer_facteur_global_initial(factor):
    """
    Applique un facteur de zoom global sur le canvas autour du centre de la fenêtre.
    """
    global facteur_global
    facteur_global = factor

    if canva:
        center_x = CANVAS_LARGEUR / 2
        center_y = CANVAS_HAUTEUR / 2

        canva.scale("all", center_x, center_y, factor, factor)

        # Centrer la vue visuellement après le zoom
        canva.xview_moveto(0.5)
        canva.yview_moveto(0.5)

    update_label_zoom()

def appliquer_parametres_si_disponible(parametres):
    if parametres and callbacks.get("set_parametres"):
        callbacks["set_parametres"](parametres)

def create_point(x, y):
    point = canva.create_rectangle(x - TAILLE_POINT, y - TAILLE_POINT, x + TAILLE_POINT, y + TAILLE_POINT, fill=COULEUR_POINT)
    update_label_compteur()
    return point

def reafficher_les_aretes():
    if canva:
        for item in canva.find_all():
            if canva.type(item) == "line":
                canva.delete(item)

        for i in range(len(sommets)):
            for j in range(i + 1, len(sommets)):
                if callbacks.get("is_connected") and callbacks["is_connected"](sommets[i], sommets[j]):
                    center1 = geo.get_center(canva.coords(sommets[i]))
                    center2 = geo.get_center(canva.coords(sommets[j]))
                    canva.create_line(center1[0], center1[1], center2[0], center2[1], fill=COULEUR_ARETE, width=2)

    update_label_compteur()

def corriger_taille_points_apres_scale(factor):
    if canva:
        for sommet in sommets:
            if canva.type(sommet) == "rectangle":
                x1, y1, x2, y2 = canva.coords(sommet)
                center_x = (x1 + x2) / 2
                center_y = (y1 + y2) / 2
                largeur = (x2 - x1) / factor
                hauteur = (y2 - y1) / factor
                canva.coords(
                    sommet,
                    center_x - largeur / 2,
                    center_y - hauteur / 2,
                    center_x + largeur / 2,
                    center_y + hauteur / 2
                )

def zoom(factor):
    global facteur_global
    if canva:
        # Trouver le centre visible de la vue actuelle
        x0 = canva.canvasx(CANVAS_LARGEUR / 2)
        y0 = canva.canvasy(CANVAS_HAUTEUR / 2)

        canva.scale("all", x0, y0, factor, factor)
        corriger_taille_points_apres_scale(factor)

        facteur_global *= factor
        update_label_zoom()

def zoom_in():
    zoom(ZOOM_IN_FACTOR)

def zoom_out():
    zoom(ZOOM_OUT_FACTOR)

def put_point(x, y):
    point = create_point(x, y)
    sommets.append(point)
    reafficher_les_aretes()

def is_drag(event):
    x = canva.canvasx(event.x)
    y = canva.canvasy(event.y)
    for point in sommets:
        x1, y1, x2, y2 = canva.coords(point)
        if x1 <= x <= x2 and y1 <= y <= y2:
            on_drag_start(x, y, point)
            return
    put_point(x, y)

def on_drag_start(x, y, point):
    global point_deplace, derniere_pos_souris
    point_deplace = point
    derniere_pos_souris = (x, y)

def on_drag_motion(event):
    global point_deplace, derniere_pos_souris
    if point_deplace is not None:
        x = canva.canvasx(event.x)
        y = canva.canvasy(event.y)
        dx = x - derniere_pos_souris[0]
        dy = y - derniere_pos_souris[1]
        canva.move(point_deplace, dx, dy)

        derniere_pos_souris = (x, y)
        reafficher_les_aretes()

def on_drag_end(event):
    global point_deplace
    point_deplace = None

def on_right_click(event):
    x = canva.canvasx(event.x)
    y = canva.canvasy(event.y)
    click_coords = (x, y)
    target = fm.find_closest_point(click_coords, sommets, canva.coords)
    if target is not None:
        remove_edges(target)
        canva.delete(target)
        sommets.remove(target)
    update_label_compteur()

def remove_edges(sommet):
    point_coords = canva.coords(sommet)
    items = canva.find_all()
    for item in items:
        if canva.type(item) == "line" and fm.is_connected(canva.coords(item), point_coords):
            canva.delete(item)
    update_label_compteur()

def changer_graphe(root):
    import interface_graphique.ui.menu_principal as mp
    global canva

    reset() 
    set_canvas(None)

    for widget in root.winfo_children():
        widget.destroy()  

    root.config(menu=None)

    mp.etat_chargement = {
        "points": [],
        "type": None,
        "parametres": {},
        "facteur_global": 1.0,
    }

    mp.ouvrir_menu(root)  

def move(direction):
    if direction == "up":
        canva.yview_scroll(-1, "units")
    elif direction == "down":
        canva.yview_scroll(1, "units")
    elif direction == "left":
        canva.xview_scroll(-1, "units")
    elif direction == "right":
        canva.xview_scroll(1, "units")

def full_reset_view():
    """Réinitialise le zoom en x1 et recadre la vue en haut à gauche"""
    global facteur_global
    if canva:
        facteur_inverse = 1 / facteur_global

        # Remettre tous les objets à l'échelle 1
        canva.scale("all", CANVAS_LARGEUR/2, CANVAS_HAUTEUR/2, facteur_inverse, facteur_inverse)
        corriger_taille_points_apres_scale(facteur_inverse)

        facteur_global = 1.0
        update_label_zoom()
        # Revenir en haut à gauche de la scrollregion
        canva.xview_moveto(0.5)
        canva.yview_moveto(0.5)
