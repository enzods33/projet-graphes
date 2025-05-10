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

from outils_canva.constantes import TAILLE_POINT, COULEUR_POINT, ZOOM_IN_FACTOR, ZOOM_OUT_FACTOR, COULEUR_ARETE, MIN_DIST, LARGEUR_ARETE, ZOOM_MIN, ZOOM_MAX, SCROLLX1, SCROLLX2, SCROLLY1, SCROLLY2
import outils_canva.geometrie as geo


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
    "get_parameters": None,
    "set_parameters": None,
    "get_graph_type": None,
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
    callbacks[nom] = fonction


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
    label_facteur_zoom.config(text=f"Zoom : x{facteur_global:.2f}")

def update_counter_label():
    """Met à jour le label qui affiche le nombre de sommets de d'arêtes"""
    nb_sommets = len(sommets)
    nb_aretes = 0
    for i in range(len(sommets)):
        for j in range(i + 1, len(sommets)):
            if callbacks.get("is_connected") and callbacks["is_connected"](i, j):
                nb_aretes += 1
    label_compteur.config(text=f"Sommets : {nb_sommets} | Arêtes : {nb_aretes}")

def reset_callbacks():
    """réinitialise les callbacks enregistrés"""
    for key in callbacks.keys():
        callbacks[key] = None

def reset():
    """
    Réinitialise complètement le canvas, les sommets, et les paramètres internes.
    """
    global sommets, facteur_global, derniere_pos_souris, point_deplace
    global unite_scroll_x, unite_scroll_y, distance_cache

    # Nettoyer les sommets
    sommets.clear()

    # Nettoyer le canvas
    if canva is not None:
        canva.delete("all")
        canva.xview_moveto(0.5)
        canva.yview_moveto(0.5)

    # Réinitialiser le label compteur
    if label_compteur:
        label_compteur.config(text="Sommets : 0 | Arêtes : 0")

    # Réinitialiser le label zoom
    if label_facteur_zoom:
        label_facteur_zoom.config(text="Zoom : x1.00")

    # Remise à zéro des variables internes
    facteur_global = 1.0
    derniere_pos_souris = None
    point_deplace = None
    unite_scroll_x = 0
    unite_scroll_y = 0
    distance_cache = {}

    # Appel au reset spécifique du graphe (si défini)
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
    if parametres and callbacks.get("set_parameters"):
        callbacks["set_parameters"](parametres)

def update_edge():
    # Supprimer d'abord toutes les anciennes lignes
    for item in canva.find_all():
        if canva.type(item) == "line":
            canva.delete(item)

    # Ensuite dessiner les nouvelles lignes selon les sommets actuels
    for i in range(len(sommets)):
        for j in range(i + 1, len(sommets)):
            if callbacks.get("is_connected") and callbacks["is_connected"](i, j):
                x1, y1 = sommets[i]
                x2, y2 = sommets[j]
                canva.create_line(
                    x1 * facteur_global, y1 * facteur_global,
                    x2 * facteur_global, y2 * facteur_global,
                    fill=COULEUR_ARETE,
                    width=LARGEUR_ARETE
                )

    update_counter_label()

def zoom(factor):
    """
    Applique un zoom sur le canvas en ajustant dynamiquement le facteur global et la scrollregion.

    Multiplie le facteur de zoom actuel par un coefficient donné,
    en respectant les limites de zoom minimum et maximum (ZOOM_MIN et ZOOM_MAX).
    Si le nouveau facteur est valide, redessine tout le contenu du canvas
    et met à jour la scrollregion pour que la zone de défilement corresponde au nouveau zoom.

    Paramètres :
        factor (float) : Coefficient de zoom (>1 pour zoom avant, <1 pour zoom arrière).
    """
    global facteur_global

    nouveau_facteur = facteur_global * factor

    if ZOOM_MIN <= nouveau_facteur <= ZOOM_MAX:
        facteur_global = nouveau_facteur
        redraw_canvas()
        update_label_zoom()

        # Mise à jour dynamique de la scrollregion après zoom
        canva.config(scrollregion=(
            SCROLLX1 * facteur_global,
            SCROLLY1 * facteur_global,
            SCROLLX2 * facteur_global,
            SCROLLY2 * facteur_global
        ))

def zoom_in():
    """zoom avant"""
    zoom(ZOOM_IN_FACTOR)

def zoom_out():
    """zoom arrière"""
    zoom(ZOOM_OUT_FACTOR)

def put_logic_point(x, y):
    sommets.append((x, y))
    redraw_canvas()

def redraw_canvas():
    if canva:
        canva.delete("all")
        for x, y in sommets:
            draw_point(x, y)
        update_edge()

def draw_point(x_logique, y_logique):
    x = x_logique * facteur_global
    y = y_logique * facteur_global
    canva.create_rectangle(
        x - TAILLE_POINT, y - TAILLE_POINT,
        x + TAILLE_POINT, y + TAILLE_POINT,
        fill=COULEUR_POINT
    )

def is_drag(event):
    """Vérifie si un point logique est déplacé, sinon ajoute un nouveau point."""
    x = canva.canvasx(event.x) / facteur_global
    y = canva.canvasy(event.y) / facteur_global

    # Adapter MIN_DIST à l'échelle actuelle
    seuil = MIN_DIST / facteur_global

    # Chercher un sommet proche du clic
    for idx, (px, py) in enumerate(sommets):
        if math.dist((x, y), (px, py)) <= seuil:
            on_drag_start(x, y, idx)
            return

    # Si aucun point proche : ajouter un nouveau point
    put_logic_point(x, y)

def on_drag_start(x, y, point):
    """initialise le déplacement d'un point"""
    global point_deplace, derniere_pos_souris
    point_deplace = point
    derniere_pos_souris = (x, y)

def on_drag_motion(event):
    """Met à jour la position du point pendant le déplacement."""
    global point_deplace, derniere_pos_souris

    if point_deplace is not None:
        x = canva.canvasx(event.x) / facteur_global
        y = canva.canvasy(event.y) / facteur_global

        dx = x - derniere_pos_souris[0]
        dy = y - derniere_pos_souris[1]

        # Déplacer le sommet logiquement
        px, py = sommets[point_deplace]
        sommets[point_deplace] = (px + dx, py + dy)

        derniere_pos_souris = (x, y)

        # Mettre à jour dynamique du cache
        for autre_idx in range(len(sommets)):
            if autre_idx != point_deplace:
                key = tuple(sorted((point_deplace, autre_idx)))
                distance_cache[key] = math.dist(sommets[point_deplace], sommets[autre_idx])

        redraw_canvas()
        update_edge()

def on_drag_end(event):
    """finalise le déplacement du point"""
    global point_deplace
    point_deplace = None

def on_right_click(event):
    """Supprime le point logique sur lequel on a fait clic droit"""
    x = canva.canvasx(event.x) / facteur_global
    y = canva.canvasy(event.y) / facteur_global
    click_coords = (x, y)

    # Adapter MIN_DIST à l'échelle actuelle
    seuil = MIN_DIST / facteur_global

    target_idx = geo.find_click_point(click_coords, sommets, seuil)

    if target_idx is not None:
        remove_edges(target_idx)
        sommets.pop(target_idx)
        redraw_canvas()

def remove_edges(idx_to_remove):
    """Supprime toutes les distances liées à un sommet supprimé (par son index) dans le cache."""
    global distance_cache

    new_cache = {}
    for (i, j), dist in distance_cache.items(): 
        if i != idx_to_remove and j != idx_to_remove:   # Si l'un des deux indices est celui qu'on veut supprimer, on ignore cette distance
            # Corriger les indices supérieurs (car la liste va perdre un élément)
            # Parce que après la suppression, tous les indices > idx_to_remove vont diminuer de 1
            ni = i - 1 if i > idx_to_remove else i
            nj = j - 1 if j > idx_to_remove else j
            new_cache[(ni, nj)] = dist

    distance_cache = new_cache

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

def full_reset_view():
    """Réinitialise le zoom en x1 et recentre la vue du canva"""
    global facteur_global, unite_scroll_x, unite_scroll_y

    # Réinitialiser le facteur de zoom
    facteur_global = 1.0
    update_label_zoom()

    # Réinitialiser les scrolls (centrer la vue)
    canva.xview_moveto(0.5)
    canva.yview_moveto(0.5)

    unite_scroll_x = 0
    unite_scroll_y = 0

    # Redessiner tous les points et arêtes au nouveau zoom (x1)
    redraw_canvas()

def get_real_distance(idx1, idx2):
    """
    Renvoie la distance réelle (corrigée du zoom) entre deux sommets (par leur index),
    en utilisant un cache pour éviter de recalculer.
    """
    key = tuple(sorted((idx1, idx2)))

    if key not in distance_cache:
        (x1, y1) = sommets[idx1]
        (x2, y2) = sommets[idx2]
        dist = math.dist((x1, y1), (x2, y2))
        distance_cache[key] = dist

    return distance_cache[key]

def add_to_cache(point_nouveau):
    """
    Calcule et ajoute toutes les distances entre le nouveau point et les autres au cache.
    """
    for autre in sommets:
        if autre != point_nouveau:
            get_real_distance(point_nouveau, autre)