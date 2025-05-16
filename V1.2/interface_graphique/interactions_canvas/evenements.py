"""
Module evenements.py

Gestion des événements souris : ajout, déplacement, suppression de sommets par clic ou drag & drop.
"""
import math
import interface_graphique.interactions_canvas.canvas_init as canvas_init
import interface_graphique.interactions_canvas.sommets as sommets
import interface_graphique.interactions_canvas.cache_distance as cache_distance
import outils_canva.outils_geometrie as geometrie
from outils_canva.constantes import MIN_DIST

point_deplace = None
derniere_pos_souris = None

def is_drag(event):
    """Détecte si un sommet existant doit être déplacé, ou si un nouveau doit être ajouté."""
    x = canvas_init.canva.canvasx(event.x) / sommets.facteur_global
    y = canvas_init.canva.canvasy(event.y) / sommets.facteur_global
    seuil = MIN_DIST / sommets.facteur_global
    for i in range(len(sommets.points)):
        px, py = sommets.points[i]
        if math.dist((x, y), (px, py)) <= seuil:
            on_drag_start(i, x, y)
            return

    sommets.put_logic_point(x, y)
    sommets.redraw_canvas()

def on_drag_start(idx_point, x, y):
    """Initialise le déplacement d'un point existant."""
    global point_deplace, derniere_pos_souris
    point_deplace = int(idx_point)
    derniere_pos_souris = (x, y)

def on_drag_motion(event):
    """Déplace un sommet existant avec la souris."""
    global point_deplace, derniere_pos_souris
    if point_deplace is None:
        return

    x = canvas_init.canva.canvasx(event.x) / sommets.facteur_global
    y = canvas_init.canva.canvasy(event.y) / sommets.facteur_global
    dx = x - derniere_pos_souris[0]
    dy = y - derniere_pos_souris[1]

    px, py = sommets.points[point_deplace]
    sommets.points[point_deplace] = (px + dx, py + dy)
    derniere_pos_souris = (x, y)

    cache_distance.refresh_point_distances(point_deplace)
    sommets.redraw_canvas()

def on_drag_end(event):
    """Termine le déplacement d'un sommet."""
    global point_deplace
    point_deplace = None

def on_right_click(event):
    """Supprime un sommet cliqué avec le bouton droit."""
    x = canvas_init.canva.canvasx(event.x) / sommets.facteur_global
    y = canvas_init.canva.canvasy(event.y) / sommets.facteur_global
    click_coords = (x, y)

    seuil = MIN_DIST / sommets.facteur_global
    idx = geometrie.find_click_point(click_coords, sommets.points, seuil)

    if idx is not None:
        sommets.points.pop(idx)
        cache_distance.remove_edges(idx)
        sommets.redraw_canvas()
