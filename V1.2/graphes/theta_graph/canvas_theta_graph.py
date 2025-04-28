import tkinter as tk

from interface_graphique import interactions_canvas as ic
from interface_graphique.ui.menu_fichier import ajouter_menu_fichier
from interface_graphique.ui.boutons import (
ajouter_bouton_changer_graphe,
ajouter_bouton_compteur,
ajouter_boutons_zoom,
ajouter_boutons_deplacement
)
from outils_canva.constantes import CANVAS_LARGEUR, CANVAS_HAUTEUR, RAYON_PAR_DEFAUT, RAYON_MODIFICATION, CANVAS_COULEUR

def ouvrir_canvas_theta_graph(root, points=None, parametres=None):
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
    #ic.enregistrer_callback('click', .left_click)
    #ic.enregistrer_callback('reset', .reset_specifique)
    #ic.enregistrer_callback('update_edges', .reafficher_les_aretes)
    #ic.enregistrer_callback('is_connected', .is_connected)
    #ic.enregistrer_callback('get_parametres', .get_parametres)
    #ic.enregistrer_callback('set_parametres', .set_parametres)
    #ic.enregistrer_callback('get_type_graphe', .get_type_graphe)
    #ic.enregistrer_callback('set_facteur_global', .set_facteur_global)

    # Association des événements clavier / souris
    canvas.bind('<Button-1>', ic.is_drag)  # clic gauche (déplacement ou ajout)
    canvas.bind('<Button-3>', ic.on_right_click)  # clic droit (suppression)
    canvas.bind('<B1-Motion>', ic.on_drag_motion)  # drag
    canvas.bind('<ButtonRelease-1>', ic.on_drag_end)  # fin de drag