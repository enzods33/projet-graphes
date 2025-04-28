"""
Module d'interface pour le graphe UDG (Unit Disk Graph).

Ce module gère l'affichage du canvas, l'initialisation de l'interface graphique,
la gestion des événements (clics, glisser-déposer, raccourcis clavier), et l'ajout
des boutons spécifiques au graphe de disques unitaires.
"""
import tkinter as tk

from interface_graphique import interactions_canvas as ic
from graphes.unit_disk_graph import interactions_unit_disk_graph as i_udg
from interface_graphique.ui.menu_fichier import ajouter_menu_fichier
from interface_graphique.ui.boutons import (
    ajouter_bouton_changer_graphe,
    ajouter_boutons_udg,
    ajouter_bouton_compteur,
    ajouter_boutons_zoom,
    ajouter_boutons_deplacement
)
from outils_canva.constantes import CANVAS_LARGEUR, CANVAS_HAUTEUR, RAYON_PAR_DEFAUT, RAYON_MODIFICATION, CANVAS_COULEUR

def ouvrir_canvas_UDG(root, points=None, parametres=None):
    """
    Initialise l'interface graphique pour un graphe de disques unitaires (UDG).

    Cette interface comprend :
    - un canvas pour afficher et manipuler les sommets et arêtes,
    - un menu pour charger/sauvegarder le graphe,
    - des boutons pour changer de graphe, ajuster le rayon, zoomer et déplacer la vue,
    - un compteur de sommets/arêtes.

    Si des points et paramètres sont fournis, ils sont automatiquement appliqués.

    Paramètres :
        root : Tkinter.Tk
            Fenêtre principale.
        points : list[tuple[float, float]], optionnel
            Liste de sommets à afficher au démarrage.
        parametres : dict, optionnel
            Paramètres du graphe.
    """
    # Réinitialiser l'affichage de la fenêtre principale
    for widget in root.winfo_children():
        widget.destroy()

    # Créer le frame principal
    frame_principal = tk.Frame(root)
    frame_principal.pack(fill=tk.BOTH, expand=True)

    # Canvas de dessin
    canvas = tk.Canvas(frame_principal, width=CANVAS_LARGEUR, height=CANVAS_HAUTEUR, background = CANVAS_COULEUR)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    canvas.focus_set()

    # Initialisation du canvas
    ic.set_canvas(canvas)

    # Menu fichier (sauvegarde / chargement)
    ajouter_menu_fichier(root)

    # Création du panneau de boutons
    frame_boutons = tk.Frame(frame_principal, bg='#f0f0f0')
    frame_boutons.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.Y)

    # Ajout boutons spécifiques au graphe UDG
    lbl_rayon = ajouter_boutons_udg(
        frame_boutons,
        augmenter_cb=lambda: i_udg.ajuster_rayon(RAYON_MODIFICATION ),
        diminuer_cb=lambda: i_udg.ajuster_rayon(-RAYON_MODIFICATION),
        reset_cb=lambda: (i_udg.reset_specifique(), ic.reset()),
        get_lbl_text=lambda: f"Rayon : {i_udg.get_rayon()}"
    )
    i_udg.set_lbl_rayon(lbl_rayon)

    # Ajout boutons communs a tous les graphs
    ajouter_bouton_changer_graphe(frame_boutons, root)
    ajouter_boutons_zoom(frame_boutons)
    ajouter_boutons_deplacement(frame_boutons)
    label_compteur = ajouter_bouton_compteur(frame_boutons)
    ic.set_label_compteur(label_compteur)

    # Affichage des points existants (si chargés)
    if points:
        for x, y in points:
            point = ic.create_point(x, y)
            ic.sommets.append(point)
        if ic.callbacks.get('update_edges'):
            ic.callbacks['update_edges']()

    # Appliquer les paramètres une fois les callbacks bien enregistrés
    if parametres:
        if ic.callbacks.get('set_parametres'):
            ic.callbacks['set_parametres'](parametres)

    # Enregistrement des callbacks
    ic.enregistrer_callback('click', i_udg.left_click)
    ic.enregistrer_callback('reset', i_udg.reset_specifique)
    ic.enregistrer_callback('update_edges', i_udg.reafficher_les_aretes)
    ic.enregistrer_callback('is_connected', i_udg.is_connected)
    ic.enregistrer_callback('get_parametres', i_udg.get_parametres)
    ic.enregistrer_callback('set_parametres', i_udg.set_parametres)
    ic.enregistrer_callback('get_type_graphe', i_udg.get_type_graphe)
    ic.enregistrer_callback('set_facteur_global', i_udg.set_facteur_global)

    # Association des événements clavier / souris
    canvas.bind('<Button-1>', ic.is_drag)  # clic gauche (déplacement ou ajout)
    canvas.bind('<Button-3>', ic.on_right_click)  # clic droit (suppression)
    canvas.bind('<B1-Motion>', ic.on_drag_motion)  # drag
    canvas.bind('<ButtonRelease-1>', ic.on_drag_end)  # fin de drag
    canvas.bind('<Shift-=>', lambda event: i_udg.ajuster_rayon(RAYON_MODIFICATION))  # + (clavier principal)
    canvas.bind('<Key-+>', lambda event: i_udg.ajuster_rayon(RAYON_MODIFICATION))  # + (pavé numérique)
    canvas.bind('<minus>', lambda event: i_udg.ajuster_rayon(-RAYON_MODIFICATION))  # - (clavier principal)   