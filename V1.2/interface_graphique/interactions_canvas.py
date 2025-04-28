from outils_canva import geometrie as fm
from outils_canva.constantes import TAILLE_POINT, COULEUR_POINT, MOVE_STEP, ZOOM_IN_FACTOR, ZOOM_OUT_FACTOR

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

def reset_callbacks():
    """Réinitialise les callbacks en les mettant à None."""
    global callbacks
    for key in callbacks.keys():
        callbacks[key] = None
        
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

def enregistrer_callback(nom, fonction):
    """
    Enregistre un callback générique dans le dictionnaire 'callbacks'.

    Paramètres :
        nom : str, nom du callback (ex: 'click', 'reset', etc.)
        fonction : fonction à enregistrer
    """
    if nom in callbacks:
        callbacks[nom] = fonction
    else:
        raise ValueError(f"Nom de callback inconnu : {nom}")

def create_point(x, y):
    point = canva.create_rectangle(x-TAILLE_POINT, y-TAILLE_POINT, x+TAILLE_POINT, y+TAILLE_POINT, fill=COULEUR_POINT)
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
    zoom(ZOOM_IN_FACTOR)

def zoom_out():
    zoom(ZOOM_OUT_FACTOR)

def move_view(dx, dy):
    if canva:
        canva.move("all", dx, dy)

def move(direction):
    if direction == "up":
        move_view(0, -MOVE_STEP)
    elif direction == "down":
        move_view(0, MOVE_STEP)
    elif direction == "left":
        move_view(-MOVE_STEP, 0)
    elif direction == "right":
        move_view(MOVE_STEP, 0)
