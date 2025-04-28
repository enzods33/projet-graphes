"""
Module contenant les fonctions de création de boutons pour l'interface graphique.

Les boutons pour :
- changer de graphe,
- générer un nuage,
- ajuster le rayon (+/-/reset),
- zoomer et dézoomer,
- déplacer la vue.

Certains boutons (changer de graphe, générer nuage) utilisent directement leur fonction associée,
d'autres (zoom, déplacement, UDG) restent génériques.
"""

import tkinter as tk

import interface_graphique.interactions_canvas as ic
from outils_canva.generation_nuage import generer_et_sauvegarder

def ajouter_bouton_compteur(frame: tk.Frame):
    """
    Crée et ajoute un label compteur de sommets/arêtes dans la frame.

    Retourne :
        tk.Label - Le widget du compteur
    """
    label_compteur = tk.Label(frame, text="Sommets : 0 | Arêtes : 0", bg="#f0f0f0")
    label_compteur.pack(pady=10)
    return label_compteur

def ajouter_bouton_changer_graphe(frame: tk.Frame, root: tk.Tk):
    """
    Ajoute un bouton permettant de changer de graphe (retourner au menu principal).
    """
    btn = tk.Button(
        frame,
        text="Changer de graphe",
        command=lambda: ic.changer_graphe(frame, root)
    )
    btn.pack(pady=20)

def ajouter_bouton_nuage_aleatoire(frame: tk.Frame):
    """
    Ajoute un bouton pour générer un nuage de points aléatoires.
    """
    btn = tk.Button(
        frame,
        text="Générer un nuage",
        command=generer_et_sauvegarder
    )
    btn.pack(pady=20)

def ajouter_boutons_udg(frame: tk.Frame, augmenter_cb, diminuer_cb, reset_cb, get_lbl_text):
    """
    Ajoute un groupe de boutons pour ajuster le rayon du graphe UDG.

    Paramètres :
        frame : Frame Tkinter
        augmenter_cb : fonction pour augmenter le rayon
        diminuer_cb : fonction pour diminuer le rayon
        reset_cb : fonction pour réinitialiser
        get_lbl_text : fonction qui retourne le texte affiché du label ("Rayon : X")

    Retourne :
        tk.Label - Le widget label du rayon
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

def ajouter_boutons_zoom(frame: tk.Frame):
    """
    Ajoute les boutons pour zoomer et dézoomer.
    """
    frame_zoom = tk.Frame(frame, bg="#f0f0f0")
    frame_zoom.pack(pady=10)

    btn_zoom_in = tk.Button(frame_zoom, text="Zoom +", command=ic.zoom_in)
    btn_zoom_in.pack(side=tk.LEFT, padx=5)

    btn_zoom_out = tk.Button(frame_zoom, text="Zoom -", command=ic.zoom_out)
    btn_zoom_out.pack(side=tk.LEFT, padx=5)

def ajouter_boutons_deplacement(frame: tk.Frame) -> None:
    """
    Ajoute les boutons pour déplacer la vue du canvas.
    """
    frame_move = tk.Frame(frame, bg="#f0f0f0")
    frame_move.pack(pady=10)

    btn_up = tk.Button(frame_move, text="↑", command=lambda: ic.move("up"), width=3)
    btn_up.grid(row=0, column=1, pady=2)

    btn_left = tk.Button(frame_move, text="←", command=lambda: ic.move("left"), width=3)
    btn_left.grid(row=1, column=0, padx=2)

    btn_down = tk.Button(frame_move, text="↓", command=lambda: ic.move("down"), width=3)
    btn_down.grid(row=1, column=1, pady=2)

    btn_right = tk.Button(frame_move, text="→", command=lambda: ic.move("right"), width=3)
    btn_right.grid(row=1, column=2, padx=2)