import tkinter as tk
from outils_canva.constantes import TAILLE_POINT, COULEUR_POINT, MOVE_STEP, ZOOM_IN_FACTOR, ZOOM_OUT_FACTOR, COULEUR_ARETE, CANVAS_HAUTEUR, CANVAS_LARGEUR
import outils_canva.geometrie as geo
from outils_canva import geometrie as fm

# Variables globales
canva = None
sommets = []
coordonnees_reelles = {}
point_deplace = None
label_compteur = None
label_facteur_zoom = None
facteur_global = 1.0
derniere_pos_souris = None
offset_x = 0
offset_y = 0

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
    global sommets, label_compteur, label_facteur_zoom, facteur_global, canva
    global offset_x, offset_y, derniere_pos_souris, coordonnees_reelles, point_deplace

    sommets.clear()
    coordonnees_reelles.clear()

    if canva is not None:
        try:
            canva.delete("all")
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
    offset_x = 0
    offset_y = 0
    derniere_pos_souris = None
    point_deplace = None

    if callbacks.get("reset"):
        callbacks["reset"]()

def appliquer_facteur_global_initial(factor):
    global facteur_global
    facteur_global = factor
    if canva:
        canva.scale("all", CANVAS_LARGEUR/2, CANVAS_HAUTEUR/2, factor, factor)
    update_label_zoom()

def appliquer_parametres_si_disponible(parametres):
    if parametres and callbacks.get("set_parametres"):
        callbacks["set_parametres"](parametres)

def create_point(x, y):
    point = canva.create_rectangle(x - TAILLE_POINT, y - TAILLE_POINT, x + TAILLE_POINT, y + TAILLE_POINT, fill=COULEUR_POINT)
    coordonnees_reelles[point] = (x, y) 
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
        canva.scale("all", CANVAS_LARGEUR/2, CANVAS_HAUTEUR/2, factor, factor)
        corriger_taille_points_apres_scale(factor)
        facteur_global *= factor
        update_label_zoom()

def zoom_in():
    zoom(ZOOM_IN_FACTOR)

def zoom_out():
    zoom(ZOOM_OUT_FACTOR)

def put_point(event):
    point = create_point(event.x, event.y)
    sommets.append(point)
    reafficher_les_aretes()

def is_drag(event):
    for point in sommets:
        x1, y1, x2, y2 = canva.coords(point)
        if x1 <= event.x <= x2 and y1 <= event.y <= y2:
            on_drag_start(event, point)
            return
    put_point(event)

def on_drag_start(event, point):
    global point_deplace, derniere_pos_souris
    point_deplace = point
    derniere_pos_souris = (event.x, event.y)

def on_drag_motion(event):
    global point_deplace, derniere_pos_souris
    if point_deplace is not None:
        dx = event.x - derniere_pos_souris[0]
        dy = event.y - derniere_pos_souris[1]
        canva.move(point_deplace, dx, dy)

        # MAJ des coordonnées réelles
        if point_deplace in coordonnees_reelles:
            x_reel, y_reel = coordonnees_reelles[point_deplace]
            coordonnees_reelles[point_deplace] = (x_reel + dx / facteur_global, y_reel + dy / facteur_global)

        derniere_pos_souris = (event.x, event.y)
        reafficher_les_aretes()

def on_drag_end(event):
    global point_deplace
    point_deplace = None

def on_right_click(event):
    click_coords = (event.x, event.y)
    target = fm.find_closest_point(click_coords, sommets, canva.coords)
    if target is not None:
        remove_edges(target)
        canva.delete(target)
        sommets.remove(target)
        coordonnees_reelles.pop(target, None)
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

def move_view(dx, dy):
    global offset_x, offset_y, coordonnees_reelles
    if canva:
        canva.move("all", dx, dy)
        
        # update offset
        offset_x += dx / facteur_global
        offset_y += dy / facteur_global

        # Et surtout update coordonnees_reelles
        for point, (x, y) in coordonnees_reelles.items():
            coordonnees_reelles[point] = (x + dx / facteur_global, y + dy / facteur_global)

def move(direction):
    if direction == "up":
        move_view(0, -MOVE_STEP)
    elif direction == "down":
        move_view(0, MOVE_STEP)
    elif direction == "left":
        move_view(-MOVE_STEP, 0)
    elif direction == "right":
        move_view(MOVE_STEP, 0)