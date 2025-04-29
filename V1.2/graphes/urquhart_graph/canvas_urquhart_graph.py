import tkinter as tk

from interface_graphique import interactions_canvas as ic
from interface_graphique.ui.menu_fichier import ajouter_menu_fichier
from interface_graphique.ui.boutons import (
    ajouter_boutons_commun
)
from outils_canva.constantes import CANVAS_LARGEUR, CANVAS_HAUTEUR, CANVAS_COULEUR
from graphes.urquhart_graph import interactions_urquhart_graph as i_ug

def ouvrir_canvas_urquhart_graph(root):
    # Réinitialiser l'affichage de la fenêtre principale
    for widget in root.winfo_children():
        widget.destroy()

    # Créer le frame principal
    frame_principal = tk.Frame(root)
    frame_principal.pack(fill=tk.BOTH, expand=True)

    # Canvas de dessin
    canvas = tk.Canvas(frame_principal, width=CANVAS_LARGEUR, height=CANVAS_HAUTEUR, background=CANVAS_COULEUR)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    canvas.focus_set()

    # Initialisation du canvas
    ic.set_canvas(canvas)

    # Menu fichier (sauvegarde / chargement)
    ajouter_menu_fichier(root)

    # Création du panneau de boutons
    frame_boutons = tk.Frame(frame_principal, bg='#f0f0f0')
    frame_boutons.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.Y)

    # Ajout boutons communs à tous les graphes
    ajouter_boutons_commun(frame_boutons, root)

    # Enregistrement des callbacks
    ic.enregistrer_callback('is_connected', i_ug.is_connected)
    ic.enregistrer_callback('get_type_graphe', i_ug.get_type_graphe)

    # Association des événements clavier / souris
    canvas.bind('<Button-1>', ic.is_drag)
    canvas.bind('<Button-3>', ic.on_right_click)
    canvas.bind('<B1-Motion>', ic.on_drag_motion)
    canvas.bind('<ButtonRelease-1>', ic.on_drag_end)
