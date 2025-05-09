"""
Module de création d'une interface graphique avec un canevas pour afficher un graphe.
"""


import tkinter as tk
from interface_graphique import interactions_canvas as ic
from interface_graphique.ui.menu_fichier import add_file_menu
from interface_graphique.ui.boutons import add_common_buttons

def create_graph(root, config_callbacks, ajouter_boutons_specifiques=None, graph_name=''):
    """
    Crée un canvas de graphe générique avec tous les éléments communs.
    Paramètres :
    root : fenêtre principale
    config_callbacks : dictionnaire {nom_callback: fonction}
    ajouter_boutons_specifiques : fonction(frame_boutons) -> ajoute les boutons spécifiques à ce graphe
    le nom du graphe
    """
    # réinitialiser la fenêtre
    for widget in root.winfo_children():
        widget.destroy()

    frame_principal = tk.Frame(root)
    frame_principal.pack(fill=tk.BOTH, expand=True)

    # Canvas
    from outils_canva.constantes import CANVAS_LARGEUR, CANVAS_HAUTEUR, CANVAS_COULEUR, SCROLLX1, SCROLLX2, SCROLLY1, SCROLLY2
    canvas = tk.Canvas(frame_principal, width=CANVAS_LARGEUR, height=CANVAS_HAUTEUR, background=CANVAS_COULEUR)
    canvas.config(scrollregion=(SCROLLX1, SCROLLY1, SCROLLX2, SCROLLY2))
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    canvas.focus_set()

    # Définir le canvas pour le module
    ic.set_canvas(canvas)
    
    add_file_menu(root)

    # Panneau boutons
    frame_boutons = tk.Frame(frame_principal, bg='#f0f0f0')
    frame_boutons.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.Y)

    if graph_name:
        label_graph = tk.Label(frame_boutons, text=f"Graphe: \n {graph_name}", font=("Helvetica", 8 ), bg='#f0f0f0')
        label_graph.pack()

    if ajouter_boutons_specifiques:
        ajouter_boutons_specifiques(frame_boutons)
    add_common_buttons(frame_boutons, root)

    # Callbacks
    for nom, fonction in config_callbacks.items():
        ic.save_callback(nom, fonction)

    # Événements
    canvas.bind('<Button-1>', ic.is_drag)
    canvas.bind('<Button-3>', ic.on_right_click)
    canvas.bind('<B1-Motion>', ic.on_drag_motion)
    canvas.bind('<ButtonRelease-1>', ic.on_drag_end)