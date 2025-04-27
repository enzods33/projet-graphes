import tkinter as tk
from outils_canva import geometrie as fm

# Variables globales
canva = None
sommets = []
point_deplace = None
label_compteur = None

derniere_pos_souris = None

callbacks = {
    "click": None,
    "reset": None,
    "update_edges": None,
    "is_connected": None,
    "get_parametres": None,
    "set_parametres": None,
    "get_type_graphe": None,
    "set_facteur_global": None,  
}

def set_label_compteur(label):
    global label_compteur
    label_compteur = label
    update_compteur()

def update_compteur():
    if label_compteur and canva:
        nb_sommets = len(sommets)
        nb_aretes = 0
        for i in range(len(sommets)):
            for j in range(i+1, len(sommets)):
                if callbacks.get("is_connected") and callbacks["is_connected"](sommets[i], sommets[j]):
                    nb_aretes += 1
        label_compteur.config(text=f"Sommets : {nb_sommets} | Arêtes : {nb_aretes}")

def set_canvas(canvas):
    global canva
    canva = canvas

def reset():
    global sommets
    sommets.clear()
    if canva:
        canva.delete("all")
    if callbacks.get("reset"):
        callbacks["reset"]()
    update_compteur()

def enregistrer_callback_get_type_graphe(func):
    callbacks["get_type_graphe"] = func

def enregistrer_callback_get_parametres(func):
    callbacks["get_parametres"] = func

def enregistrer_callback_set_parametres(func):
    callbacks["set_parametres"] = func

def enregistrer_callback_is_connected(func):
    callbacks["is_connected"] = func

def enregistrer_callback_click(func):
    callbacks["click"] = func

def enregistrer_callback_reset(func):
    callbacks["reset"] = func

def enregistrer_callback_update_edges(func):
    callbacks["update_edges"] = func

def enregistrer_callback_set_facteur_global(func):
    callbacks["set_facteur_global"] = func

def create_point(x, y):
    point = canva.create_rectangle(x-3, y-3, x+3, y+3, fill="yellow")
    update_compteur()
    return point

def on_right_click(event):
    click_coords = (event.x, event.y)
    target = fm.find_closest_point(click_coords, sommets, canva.coords)
    if target is not None:
        remove_edges(target)
        canva.delete(target)
        sommets.remove(target)
    update_compteur()

def remove_edges(sommet):
    point_coords = canva.coords(sommet)
    items = canva.find_all()
    for item in items:
        if canva.type(item) == "line" and fm.is_connected(canva.coords(item), point_coords):
            canva.delete(item)
    update_compteur()

def is_drag(event):
    for point in sommets:
        x1, y1, x2, y2 = canva.coords(point)
        if x1 <= event.x <= x2 and y1 <= event.y <= y2:
            on_drag_start(event, point)
            return

    if callbacks["click"]:
        callbacks["click"](event)
    if callbacks["update_edges"]:
        callbacks["update_edges"]()

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
        derniere_pos_souris = (event.x, event.y)

        if callbacks["update_edges"]:
            callbacks["update_edges"]()

def on_drag_end(event):
    global point_deplace
    if point_deplace is not None:
        point_deplace = None

def changer_graphe(frame_actuel, root):
    reset()
    if callbacks.get("reset"):
        callbacks["reset"]()
    frame_actuel.destroy()

    from interface_graphique.ui.menu_principal import ouvrir_menu
    ouvrir_menu(root)

def couples_som():
    pass

def appliquer_parametres_si_disponible(parametres):
    if parametres and callbacks.get("set_parametres"):
        callbacks["set_parametres"](parametres)
    if callbacks.get("update_edges"):
        callbacks["update_edges"]()

def zoom(factor):
    if canva:
        canva.scale("all", 0, 0, factor, factor)

        # Redimensionner chaque sommet (rectangle)
        for sommet in sommets:
            if canva.type(sommet) == "rectangle":
                x1, y1, x2, y2 = canva.coords(sommet)
                center_x = (x1 + x2) / 2
                center_y = (y1 + y2) / 2

                # Ici ON NE MULTIPLIE PAS LE WIDTH par le factor
                # On fait l'inverse de ce qu'on a fait visuellement
                largeur = (x2 - x1) / factor
                hauteur = (y2 - y1) / factor

                canva.coords(
                    sommet,
                    center_x - largeur / 2,
                    center_y - hauteur / 2,
                    center_x + largeur / 2,
                    center_y + hauteur / 2)

        if callbacks.get("set_facteur_global"):
            callbacks["set_facteur_global"](factor)

        if callbacks.get("update_edges"):
            callbacks["update_edges"]()

def zoom_in():
    zoom(1.1)

def zoom_out():
    zoom(0.9)

def move_view(dx, dy):
    if canva:
        canva.move("all", dx, dy)

def move_up():
    move_view(0, -20)

def move_down():
    move_view(0, 20)

def move_left():
    move_view(-20, 0)

def move_right():
    move_view(20, 0)
