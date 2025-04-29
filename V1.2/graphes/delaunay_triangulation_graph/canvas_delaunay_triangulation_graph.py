import tkinter as tk

from interface_graphique import interactions_canvas as ic
from interface_graphique.ui.menu_fichier import ajouter_menu_fichier
from interface_graphique.ui.boutons import (
    ajouter_bouton_changer_graphe,
    ajouter_boutons_zoom,
    ajouter_boutons_deplacement,
    ajouter_bouton_compteur,
    ajouter_boutons_reset
)
from outils_canva.constantes import CANVAS_LARGEUR, CANVAS_HAUTEUR, CANVAS_COULEUR
from graphes.delaunay_triangulation_graph import interactions_delaunay_triangulation_graph as i_dt

def ouvrir_canvas_delaunay_triangulation_graph(root):
    for widget in root.winfo_children():
        widget.destroy()

    frame_principal = tk.Frame(root)
    frame_principal.pack(fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(frame_principal, width=CANVAS_LARGEUR, height=CANVAS_HAUTEUR, background=CANVAS_COULEUR)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    canvas.focus_set()

    ic.set_canvas(canvas)

    ajouter_menu_fichier(root)

    frame_boutons = tk.Frame(frame_principal, bg='#f0f0f0')
    frame_boutons.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.Y)

    ajouter_bouton_changer_graphe(frame_boutons, root)
    ajouter_boutons_zoom(frame_boutons)
    ajouter_bouton_compteur(frame_boutons)
    ajouter_boutons_deplacement(frame_boutons)
    ajouter_boutons_reset(frame_boutons, ic.reset)

    ic.enregistrer_callback('is_connected', i_dt.is_connected)
    ic.enregistrer_callback('get_type_graphe', i_dt.get_type_graphe)

    canvas.bind('<Button-1>', ic.is_drag)
    canvas.bind('<Button-3>', ic.on_right_click)
    canvas.bind('<B1-Motion>', ic.on_drag_motion)
    canvas.bind('<ButtonRelease-1>', ic.on_drag_end)
