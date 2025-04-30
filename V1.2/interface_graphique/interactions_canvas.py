"""
Module de gestion du canevas et des interactions graphiques pour un graphe.
Contient des fonctions permettant de gérer un canevas dans une interface Tkinter pour afficher 
et manipuler un graphe. 
Les fonctions permettent:
- la création de points (sommets) et d'arêtes (lignes reliant les points)
- zoomer, plus et moins
- drag and drop
- clics de la souris
- sauvegarde et gestion des distances entre les sommets dans un cache, pour optimiser, car trop de lag
- gestion de l'affichage des informations sur les sommets et les arêtes avec des labels
"""
import tkinter as tk
import math

from outils_canva.constantes import TAILLE_POINT, COULEUR_POINT, ZOOM_IN_FACTOR, ZOOM_OUT_FACTOR, COULEUR_ARETE, CANVAS_HAUTEUR, CANVAS_LARGEUR, MIN_DIST
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
unite_scroll_x = 0
unite_scroll_y = 0
distance_cache = {}  # clé : tuple trié (id1, id2) → valeur : distance réelle

callbacks = {
    "reset": None,
    "is_connected": None,
    "get_parametres": None,
    "set_parametres": None,
    "get_type_graphe": None,
}

def set_canvas(canvas):
    """Initialise le canvas pour pouvoir interagir avec"""
    global canva
    canva = canvas

def save_callback(nom, fonction):
    """
    Sauvegarde un callback
    Paramètres :
        nom: nom du callback à sauvegarder
        fonction: la fonction à appeler pour ce callback.
    """
    if nom in callbacks:
        callbacks[nom] = fonction
    else:
        raise ValueError(f"Nom de callback inconnu : {nom}")

def set_label_compteur(label):
    """
    Définit le label de comptage des sommets et des arêtes.
    Paramètres :
        label: le label Tkinter qui afficher le comptage des sommets et des arêtes
    """
    global label_compteur
    label_compteur = label
    update_counter_label()

def set_label_zoom(label):
    """
    Définit le label affichant le facteur de zoom actuel
    Paramètres:
        label: le label Tkinter qui afficher le facteur zoom.
    """
    global label_facteur_zoom
    label_facteur_zoom = label
    update_label_zoom()

def update_label_zoom():
    """Met à jour le label quui affiche le facteur de zoom actuel"""
    if label_facteur_zoom:
        label_facteur_zoom.config(text=f"Zoom : x{facteur_global:.2f}")

def update_counter_label():
    """Met à jour le label qui affiche le nombre de sommets de d'arêtes"""
    if label_compteur and canva:
        nb_sommets = len(sommets)
        nb_aretes = 0
        for i in range(len(sommets)):
            for j in range(i + 1, len(sommets)):
                if callbacks.get("is_connected") and callbacks["is_connected"](sommets[i], sommets[j]):
                    nb_aretes += 1
        label_compteur.config(text=f"Sommets : {nb_sommets} | Arêtes : {nb_aretes}")

def reset_callbacks():
    """réinitialise les callbacks enregistrés"""
    for key in callbacks.keys():
        callbacks[key] = None

def reset():
    """
    réinitialise tout le canva et les paramètres:
    les sommets, le facteur de zoom, les labels, la position de la souris, le cahce des distances
    """
    global sommets, label_compteur, label_facteur_zoom, facteur_global, canva, derniere_pos_souris, point_deplace
    global unite_scroll_x, unite_scroll_y, distance_cache

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
    unite_scroll_x = 0
    unite_scroll_y = 0
    distance_cache = {} 

    if callbacks.get("reset"):
        callbacks["reset"]()

def apply_intial_global_factor(factor):
    """
    Applique un facteur de zoom global factor sur le canvas autour du centre de la fenêtre.
    Paramètres:
        factor: le facteur de zoom à appliquer    
    """
    global facteur_global
    facteur_global = factor
    update_label_zoom()

def apply_parameters_if_posible(parametres):
    """
    applique des paramètres spécifiques au graphe si c'est possible
    Paramètres:
        parametres: dictionnaire des paramètres à appliquer
    """
    if parametres and callbacks.get("set_parametres"):
        callbacks["set_parametres"](parametres)

def create_point(x, y):
    """
    Crée un point (un sommet) sur le canva aux coordonées x et y
    Paramètres :
        x, y : les coordonnées en abscisse et ordonnée du point à créer
    Retour :
        point: l'ID du point créé sur le canvas.
    """
    point = canva.create_rectangle(x - TAILLE_POINT, y - TAILLE_POINT, x + TAILLE_POINT, y + TAILLE_POINT, fill=COULEUR_POINT)
    update_counter_label()
    return point

def update_edge():
    """met à jour les arêtes entre les sommets"""
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

    update_counter_label()

def update_point_size(factor):
    """
    met à jour la taille des points en fonctoin du facteur factor de zoom
    Paramètres:
        factor: facteur de zoom actuel
    """
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
    """
    applique un zoom de facteur factor sur le canva
    Paramètres:
        factor: facteur de zoom 
    """
    global facteur_global
    if canva:
        # Trouver le centre visible de la vue actuelle
        x0 = canva.canvasx(CANVAS_LARGEUR / 2)
        y0 = canva.canvasy(CANVAS_HAUTEUR / 2)

        canva.scale("all", x0, y0, factor, factor)
        update_point_size(factor)

        facteur_global *= factor
        update_label_zoom()

def zoom_in():
    """zoom avant"""
    zoom(ZOOM_IN_FACTOR)

def zoom_out():
    """zoom arrière"""
    zoom(ZOOM_OUT_FACTOR)

def put_point(x, y):
    """ajoute un point au canva aux coordonées x,y et met a jour les arêtes"""
    point = create_point(x, y)
    sommets.append(point)
    add_to_cache(point)
    update_edge()

def is_drag(event):
    """vérifie si un point est en train d'être déplacé"""
    x = canva.canvasx(event.x)
    y = canva.canvasy(event.y)
    for point in sommets:
        x1, y1, x2, y2 = canva.coords(point)
        if x1 <= x <= x2 and y1 <= y <= y2:
            on_drag_start(x, y, point)
            return
    put_point(x, y)

def on_drag_start(x, y, point):
    """initialise le déplacement d'un point"""
    global point_deplace, derniere_pos_souris
    point_deplace = point
    derniere_pos_souris = (x, y)

def on_drag_motion(event):
    """met à jour la position du point pendant le déplacement"""
    global point_deplace, derniere_pos_souris
    if point_deplace is not None:
        x = canva.canvasx(event.x)
        y = canva.canvasy(event.y)
        dx = x - derniere_pos_souris[0]
        dy = y - derniere_pos_souris[1]
        canva.move(point_deplace, dx, dy)
        derniere_pos_souris = (x, y)

        # Mise à jour dynamique du cache
        for autre in sommets:
            if autre != point_deplace:
                key = tuple(sorted((point_deplace, autre)))
                c1 = geo.get_center(canva.coords(point_deplace))
                c2 = geo.get_center(canva.coords(autre))
                dist = math.dist(c1, c2) / facteur_global
                distance_cache[key] = dist

        update_edge()

def on_drag_end(event):
    """finalise le déplacement du point"""
    global point_deplace
    point_deplace = None

def on_right_click(event):
    """supprime le point sur lequel on a clic droit"""
    x = canva.canvasx(event.x)
    y = canva.canvasy(event.y)
    click_coords = (x, y)
    target = fm.find_click_point(click_coords, sommets, canva.coords, MIN_DIST)
    if target is not None:
        remove_edges(target)
        canva.delete(target)
        sommets.remove(target)
    update_edge()
    update_counter_label()

def remove_edges(sommet):
    """supprime les arêtes liées à un sommet (sommet) supprimé"""
    global distance_cache
    point_coords = canva.coords(sommet)
    items = canva.find_all()
    for item in items:
        if canva.type(item) == "line" and fm.is_connected(canva.coords(item), point_coords):
            canva.delete(item)

    # Supprimer les distances liées à ce point
    distance_cache = {
        (i, j): d for (i, j), d in distance_cache.items()
        if i != sommet and j != sommet
    }

    update_counter_label()

def change_graph(root):
    """change de graphe et réinitialise le canva"""
    import interface_graphique.ui.menu_principal as mp
    global canva

    reset() 
    set_canvas(None)

    for widget in root.winfo_children():
        widget.destroy()  

    root.config(menu=None)

    mp.reset_loading_state()
    mp.open_menu(root)  

def move(direction):
    """déplace la vue du canva dans la direction direction"""
    global unite_scroll_x, unite_scroll_y

    if direction == "up":
        before = canva.yview()
        canva.yview_scroll(-1, "units")
        if canva.yview() != before:
            unite_scroll_y -= 1

    elif direction == "down":
        before = canva.yview()
        canva.yview_scroll(1, "units")
        if canva.yview() != before:
            unite_scroll_y += 1

    elif direction == "left":
        before = canva.xview()
        canva.xview_scroll(-1, "units")
        if canva.xview() != before:
            unite_scroll_x -= 1

    elif direction == "right":
        before = canva.xview()
        canva.xview_scroll(1, "units")
        if canva.xview() != before:
            unite_scroll_x += 1

def full_reset_view():
    """Réinitialise le zoom en x1 et recentre la vue du canva"""
    global facteur_global, unite_scroll_x, unite_scroll_y
    if canva:
        facteur_inverse = 1 / facteur_global

        # Remettre tous les objets à l'échelle 1
        canva.scale("all", CANVAS_LARGEUR/2, CANVAS_HAUTEUR/2, facteur_inverse, facteur_inverse)
        update_point_size(facteur_inverse)

        facteur_global = 1.0
        update_label_zoom()
        
        # Revenir en haut à gauche de la scrollregion
        canva.xview_moveto(0.5)
        canva.yview_moveto(0.5)
        unite_scroll_x = 0
        unite_scroll_y = 0

def get_real_distance(p1, p2):
    """
    Renvoie la distance réelle (corrigée du zoom) entre deux sommets, avec cache, seulement si elle n'a pas déja été calculée.
    """
    key = tuple(sorted((p1, p2)))
    if key not in distance_cache:
        c1 = geo.get_center(canva.coords(p1))
        c2 = geo.get_center(canva.coords(p2))
        dist = math.dist(c1, c2) / facteur_global
        distance_cache[key] = dist
    return distance_cache[key]

def add_to_cache(point_nouveau):
    """
    Calcule et ajoute toutes les distances entre le nouveau point et les autres au cache.
    """
    for autre in sommets:
        if autre != point_nouveau:
            get_real_distance(point_nouveau, autre)