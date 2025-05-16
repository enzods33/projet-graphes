"""
Module zoom.py

Gestion du zoom sur le canvas : zoom avant/arrière, mise à jour du facteur global et de la scrollregion.
"""

import interface_graphique.interactions_canvas.canvas_init as canvas_init
import interface_graphique.interactions_canvas.sommets as sommets
from outils_canva.constantes import ZOOM_IN_FACTOR, ZOOM_OUT_FACTOR, ZOOM_MIN, ZOOM_MAX, SCROLLX1, SCROLLX2, SCROLLY1, SCROLLY2

def zoom(factor):
    """Applique un zoom avec un facteur donné."""
    nouveau_facteur = sommets.facteur_global * factor
    if ZOOM_MIN <= nouveau_facteur <= ZOOM_MAX:
        sommets.facteur_global = nouveau_facteur
        sommets.redraw_canvas()
        update_zoom_label()
        refresh_scrollregion()

def zoom_in():
    """Zoom avant."""
    zoom(ZOOM_IN_FACTOR)

def zoom_out():
    """Zoom arrière."""
    zoom(ZOOM_OUT_FACTOR)

def refresh_scrollregion():
    """Met à jour la zone de scroll du canvas."""
    if canvas_init.canva:
        canvas_init.canva.config(scrollregion=(
            SCROLLX1 * sommets.facteur_global,
            SCROLLY1 * sommets.facteur_global,
            SCROLLX2 * sommets.facteur_global,
            SCROLLY2 * sommets.facteur_global
        ))

def update_zoom_label():
    """Met à jour l'affichage du facteur de zoom."""
    if canvas_init.label_facteur_zoom and canvas_init.label_facteur_zoom.winfo_exists():
        canvas_init.label_facteur_zoom.config(text=f"Zoom : x{sommets.facteur_global:.2f}")

def apply_intial_global_factor(factor):
    """Applique un facteur global initial de zoom sur le canvas."""
    sommets.facteur_global = factor
    update_zoom_label()
    refresh_scrollregion()
    sommets.redraw_canvas()
