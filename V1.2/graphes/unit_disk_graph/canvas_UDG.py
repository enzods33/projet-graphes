"""
Module d'interface pour le graphe UDG (Unit Disk Graph).

Ce module gère l'affichage du canvas, l'initialisation de l'interface graphique,
la gestion des événements (clics, glisser-déposer, raccourcis clavier), et l'ajout
des boutons spécifiques au graphe de disques unitaires.
"""
import tkinter as tk
from interface_graphique import interactions_canvas as ic
from graphes.unit_disk_graph import interactions_UDG as i_udg
from interface_graphique.menu_fichier import ajouter_menu_fichier

def ouvrir_canvas_UDG(root, points=None):
    """
    Ouvre et initialise l'interface du graphe de disques unitaires (UDG).

    Cette interface contient :
    - un canvas graphique pour dessiner et déplacer les sommets,
    - un menu pour charger ou sauvegarder les points,
    - des boutons pour changer de graphe, ajuster le rayon et réinitialiser.

    Si des points sont fournis, ils sont automatiquement affichés à l'ouverture.

    Paramètres :
        root : fenêtre principale Tkinter.
        points : liste optionnelle de tuples (x, y) représentant des sommets à afficher dès le départ.
    """
    # Créer le frame principal
    frame_principal = tk.Frame(root)
    frame_principal.pack(fill=tk.BOTH, expand=True)

    # Canvas de dessin
    canvas = tk.Canvas(frame_principal, width=600, height=600, background="white")
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    canvas.focus_set()

    # Initialisation du canvas
    ic.set_canvas(canvas)

    # Enregistrement des callbacks via le dictionnaire centralisé
    ic.enregistrer_callback_click(i_udg.left_click)
    ic.enregistrer_callback_reset(i_udg.reset_specifique)
    ic.enregistrer_callback_update_edges(i_udg.reafficher_les_arêtes)

    # Menu fichier (sauvegarde / chargement)
    ajouter_menu_fichier(root)

    # Création du panneau de boutons
    frame_boutons = tk.Frame(frame_principal, bg="#f0f0f0")
    frame_boutons.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.Y)
    i_udg.add_controls(frame_boutons)
    ic.add_button_change_graph(frame_boutons, root)

    # Affichage des points chargés (le cas échéant)
    if points:
        for x, y in points:
            point = ic.create_point(x, y)
            ic.sommets.append(point)
        if ic.callbacks["update_edges"]:
            ic.callbacks["update_edges"]()

    # Association des événements clavier / souris
    canvas.bind("<Button-1>", ic.is_drag)               # clic gauche (déplacement ou ajout)
    canvas.bind("<Button-3>", ic.on_right_click)        # clic droit (suppression)
    canvas.bind("<B1-Motion>", ic.on_drag_motion)       # drag
    canvas.bind("<ButtonRelease-1>", ic.on_drag_end)    # fin de drag
    canvas.bind("<Shift-=>", i_udg.augmenter_rayon)     # + (clavier principal)
    canvas.bind("<Key-+>", i_udg.augmenter_rayon)       # + (pavé numérique)
    canvas.bind("<minus>", i_udg.diminuer_rayon)        # - (clavier principal)
    canvas.bind("<Key-->", i_udg.diminuer_rayon)        # - (pavé numérique)