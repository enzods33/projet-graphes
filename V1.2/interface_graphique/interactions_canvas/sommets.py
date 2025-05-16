"""
Module sommets.py

Gestion des points (sommets), dessin, compteur et arêtes sur le canvas.
"""

import interface_graphique.interactions_canvas.canvas_init as canvas_init
from interface_graphique.interactions_canvas import cache_distance
import interface_graphique.interactions_canvas.sommets as sommets
from outils_canva.constantes import TAILLE_POINT, COULEUR_POINT, COULEUR_ARETE, LARGEUR_ARETE

points = []
facteur_global = 1.0

def put_logic_point(x, y):
    """Ajoute un point logique."""
    global points
    from outils_canva.constantes import MAX_NB_POINTS
    if len(points) < MAX_NB_POINTS:
        points.append((x, y))
        cache_distance.add_to_cache(len(sommets.points) - 1)

def draw_point(x_logique, y_logique):
    """Dessine un point sur le canvas."""
    x = x_logique * facteur_global
    y = y_logique * facteur_global
    canvas_init.canva.create_rectangle(
        x - TAILLE_POINT, y - TAILLE_POINT,
        x + TAILLE_POINT, y + TAILLE_POINT,
        fill=COULEUR_POINT
    )

def redraw_canvas():
    """Redessine entièrement les points et arêtes."""
    if canvas_init.canva:
        canvas_init.canva.delete("all")
        for x, y in points:
            draw_point(x, y)
        update_edge()
        update_counter_label()

def update_edge():
    """Dessine les arêtes entre sommets selon le callback is_connected."""
    if canvas_init.callbacks["is_connected"]:
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if canvas_init.callbacks["is_connected"](i, j):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    canvas_init.canva.create_line(
                        x1 * facteur_global, y1 * facteur_global,
                        x2 * facteur_global, y2 * facteur_global,
                        fill=COULEUR_ARETE,
                        width=LARGEUR_ARETE
                    )

def update_counter_label():
    """Met à jour l'affichage du nombre de sommets et d'arêtes."""
    nb_sommets = len(points)
    nb_aretes = 0
    if canvas_init.callbacks["is_connected"]:
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if canvas_init.callbacks["is_connected"](i, j):
                    nb_aretes += 1

    if canvas_init.label_compteur and canvas_init.label_compteur.winfo_exists():
        canvas_init.label_compteur.config(text=f"Sommets : {nb_sommets}\nArêtes : {nb_aretes}")
