"""
Module contenant les fonctions de création de boutons pour l'interface graphique.

Les fonctions ici ajoutent des boutons à une frame Tkinter et définissent
les comportements associés (callback, navigation, reset, etc.).
"""

import tkinter as tk

def ajouter_bouton_compteur(frame):
    """
    Crée et ajoute un label compteur de sommets/arêtes dans la frame fournie.

    Retourne le widget label pour mise à jour ultérieure.
    """
    label_compteur = tk.Label(frame, text="Sommets : 0 | Arêtes : 0", bg="#f0f0f0")
    label_compteur.pack(pady=10)
    return label_compteur

def ajouter_bouton_changer_graphe(frame, root, changer_callback):
    """
    Ajoute un bouton permettant de revenir au menu principal.

    Paramètres :
        frame : Frame Tkinter où ajouter le bouton
        root : Fenêtre principale Tkinter
        changer_callback : fonction à appeler quand on clique sur le bouton
    """
    btn = tk.Button(
        frame,
        text="Changer de graphe",
        command=lambda: changer_callback(frame, root)
    )
    btn.pack(pady=20)

def ajouter_boutons_udg(frame, augmenter_cb, diminuer_cb, reset_cb, get_lbl_text):
    """
    Ajoute les boutons + / - / Reset pour ajuster le rayon du graphe UDG.

    Paramètres :
        frame : Frame Tkinter
        augmenter_cb : callback pour le bouton +
        diminuer_cb : callback pour le bouton -
        reset_cb : callback pour le bouton Reset
        get_lbl_text : fonction qui retourne le texte du label ("Rayon : 100" par exemple)

    Retourne :
        Le widget label du rayon.
    """
    frame_pm = tk.Frame(frame, bg="#f0f0f0")
    frame_pm.pack(pady=10)

    btn_plus = tk.Button(frame_pm, text="+", command=augmenter_cb)
    btn_plus.pack(side=tk.RIGHT, padx=5)

    lbl_rayon = tk.Label(frame_pm, text=get_lbl_text(), bg="#f0f0f0")
    lbl_rayon.pack(side=tk.RIGHT)

    btn_moins = tk.Button(frame_pm, text="-", command=diminuer_cb)
    btn_moins.pack(side=tk.RIGHT, padx=5)

    btn_reset = tk.Button(frame, text="Reset", command=reset_cb)
    btn_reset.pack(pady=10)

    return lbl_rayon

def ajouter_bouton_nuage_aleatoire(frame, generer_callback):
    """
    Ajoute un bouton pour générer un nuage de points aléatoires.

    Paramètres :
        frame : Frame Tkinter où placer le bouton
        generer_callback : fonction à appeler quand on clique sur le bouton
    """
    btn = tk.Button(frame, text="Générer un nuage", command=generer_callback)
    btn.pack(pady=20)

def ajouter_boutons_zoom(frame, zoom_in_callback, zoom_out_callback):
    """
    Ajoute deux boutons pour zoomer et dézoomer sur le canvas.

    Paramètres :
        frame : Frame Tkinter où ajouter les boutons
        zoom_in_callback : fonction pour zoomer
        zoom_out_callback : fonction pour dézoomer
    """
    frame_zoom = tk.Frame(frame, bg="#f0f0f0")
    frame_zoom.pack(pady=10)

    btn_zoom_in = tk.Button(frame_zoom, text="Zoom +", command=zoom_in_callback)
    btn_zoom_in.pack(side=tk.LEFT, padx=5)

    btn_zoom_out = tk.Button(frame_zoom, text="Zoom -", command=zoom_out_callback)
    btn_zoom_out.pack(side=tk.LEFT, padx=5)

def ajouter_boutons_deplacement(frame, up_cb, down_cb, left_cb, right_cb):
    """
    Ajoute quatre boutons pour déplacer la vue du canvas.

    Paramètres :
        frame : Frame Tkinter pour placer les boutons
        up_cb, down_cb, left_cb, right_cb : callbacks pour chaque direction
    """
    frame_move = tk.Frame(frame, bg="#f0f0f0")
    frame_move.pack(pady=10)

    btn_up = tk.Button(frame_move, text="↑", command=up_cb, width=3)
    btn_up.grid(row=0, column=1, pady=2)

    btn_left = tk.Button(frame_move, text="←", command=left_cb, width=3)
    btn_left.grid(row=1, column=0, padx=2)

    btn_down = tk.Button(frame_move, text="↓", command=down_cb, width=3)
    btn_down.grid(row=1, column=1, pady=2)

    btn_right = tk.Button(frame_move, text="→", command=right_cb, width=3)
    btn_right.grid(row=1, column=2, padx=2)