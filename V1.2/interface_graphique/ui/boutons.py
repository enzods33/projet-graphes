"""
Module contenant les fonctions de création de boutons pour l'interface graphique.

Les fonctions ici ajoutent des boutons à une frame Tkinter et définissent
les comportements associés (callback, navigation, reset, etc.).
"""

import tkinter as tk
from interface_graphique import interactions_canvas as ic
from graphes.unit_disk_graph import interactions_UDG as i_udg

def ajouter_bouton_compteur(frame):
    """
    Crée et ajoute le label compteur de sommets/arêtes dans la frame fournie.

    Retourne le widget label pour mise à jour ultérieure.
    """
    label_compteur = tk.Label(frame, text="Sommets : 0 | Arêtes : 0", bg="#f0f0f0")
    label_compteur.pack(pady=10)
    return label_compteur

def ajouter_bouton_changer_graphe(frame, root):
    """
    Ajoute un bouton permettant de revenir au menu principal.

    Paramètres :
        frame : Frame Tkinter où ajouter le bouton
        root : Fenêtre principale Tkinter, utilisée pour réinitialiser l'affichage
    """
    btn = tk.Button(
        frame,
        text="Changer de graphe",
        command=lambda: ic.changer_graphe(frame, root)
    )
    btn.pack(pady=20)


def ajouter_boutons_udg(frame, get_lbl_text):
    """
    Ajoute les boutons spécifiques au graphe UDG : + / - / Reset, avec un label de rayon.

    Paramètres :
        frame : Frame Tkinter qui recevra les boutons
        augmenter_cb : fonction à appeler lors du clic sur '+'
        diminuer_cb : fonction à appeler lors du clic sur '-'
        reset_cb : fonction à appeler lors du clic sur 'Reset'
        get_label_text : fonction qui retourne le texte du label (ex: "Rayon : 100")

    Retour :
        Label Tkinter (widget) utilisé pour afficher le rayon, afin de pouvoir le mettre à jour.
    """
    frame_pm = tk.Frame(frame, bg="#f0f0f0")
    frame_pm.pack(pady=10)

    btn_plus = tk.Button(frame_pm, text="+", command=i_udg.augmenter_rayon)
    btn_plus.pack(side=tk.RIGHT, padx=5)

    lbl_rayon = tk.Label(frame_pm, text=get_lbl_text, bg="#f0f0f0")
    lbl_rayon.pack(side=tk.RIGHT)

    btn_moins = tk.Button(frame_pm, text="-", command=i_udg.diminuer_rayon)
    btn_moins.pack(side=tk.RIGHT, padx=5)

    btn_reset = tk.Button(frame, text="Reset", command=lambda: (i_udg.reset_specifique(), ic.reset()))
    btn_reset.pack(pady=10)

    return lbl_rayon

