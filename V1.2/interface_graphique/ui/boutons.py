"""
Module contenant les fonctions de création de boutons pour l'interface graphique.
Les boutons pour :
- changer de graphe,
- générer un nuage,
- ajuster le rayon (+/-/reset),
- zoomer et dézoomer,
- déplacer la vue,
- réinitialiser le zoom et la vue.
"""

import tkinter as tk

import interface_graphique.interactions_canvas as ic
from gen_cloud import explications

def add_common_buttons(frame, root):
    """
    fonction qui ajoute les boutons communs à tous les graphes
    """

    # Zoom
    frame_zoom = tk.Frame(frame, bg="#f0f0f0")
    frame_zoom.pack(pady=10)
    tk.Button(frame_zoom, text="Zoom +", command=ic.zoom_in).pack(side=tk.LEFT, padx=5)
    tk.Button(frame_zoom, text="Zoom -", command=ic.zoom_out).pack(side=tk.LEFT, padx=5)

    # Labels zoom
    label_zoom = tk.Label(frame, text="Zoom : x1.00", bg="#f0f0f0")
    label_zoom.pack(pady=5)
    ic.set_label_zoom(label_zoom)

    # Full reset view
    tk.Button(frame, text="Full reset view", command=ic.full_reset_view).pack(pady=10)

    # Label compteur
    label_compteur = tk.Label(frame, text="Sommets : 0 | Arêtes : 0", bg="#f0f0f0")
    label_compteur.pack(pady=10)
    ic.set_label_compteur(label_compteur)   

    # Reset
    tk.Button(frame, text="Reset", command=ic.reset).pack(pady=10)

    # Bouton "Changer de graphe"
    btn_changer = tk.Button(frame, text="Changer de graphe", command=lambda: ic.change_graph(root))
    btn_changer.pack(pady=20)

def add_udg_button(frame: tk.Frame, augmenter_cb, diminuer_cb, get_lbl_text, set_lbl_rayon_cb):
    """
    Ajoute les boutons pour modifier le rayon du unit disk graph
    Paramètres:
        frame: Frame Tkinter
        augmenter_cb: fonction pour augmenter le rayon
        diminuer_cb: fonction pour diminuer le rayon
        reset_cb: fonction pour réinitialiser
        get_lbl_text: fonction qui retourne le texte affiché du label
        set_lbl_rayon_cb: fonction pour enregistrer le label du rayon
    """
    frame_pm = tk.Frame(frame, bg="#f0f0f0")
    frame_pm.pack(pady=10)

    btn_plus = tk.Button(frame_pm, text="+", command=augmenter_cb)
    btn_plus.pack(side=tk.RIGHT, padx=5)

    lbl_rayon = tk.Label(frame_pm, text=get_lbl_text(), bg="#f0f0f0")
    lbl_rayon.pack(side=tk.RIGHT)

    set_lbl_rayon_cb(lbl_rayon)  

    btn_moins = tk.Button(frame_pm, text="-", command=diminuer_cb)
    btn_moins.pack(side=tk.RIGHT, padx=5)

def add_kcng_buttons(frame: tk.Frame, augmenter_cb, diminuer_cb, get_lbl_text, set_lbl_k_cb):
    """
    Ajoute un groupe de boutons pour ajuster la valeur de k dans un k-NN graph.
    Paramètres :
        frame : Frame Tkinter
        augmenter_cb : fonction pour augmenter k
        diminuer_cb : fonction pour diminuer k
        get_lbl_text : fonction qui retourne le texte affiché du label
        set_lbl_k_cb : fonction pour enregistrer le label
    """
    frame_k = tk.Frame(frame, bg="#f0f0f0")
    frame_k.pack(pady=10)

    btn_plus = tk.Button(frame_k, text="+", command=augmenter_cb)
    btn_plus.pack(side=tk.RIGHT, padx=5)

    lbl_k = tk.Label(frame_k, text=get_lbl_text(), bg="#f0f0f0")
    lbl_k.pack(side=tk.RIGHT)

    set_lbl_k_cb(lbl_k)

    btn_moins = tk.Button(frame_k, text="-", command=diminuer_cb)
    btn_moins.pack(side=tk.RIGHT, padx=5)

def add_theta_button(frame: tk.Frame, augmenter_cb, diminuer_cb, get_lbl_text, set_lbl_k_cb):
    """
    Ajoute les boutons pour modifier le nombre de cônes du Theta Graph.

    Paramètres:
        frame: Frame Tkinter
        augmenter_cb: fonction pour augmenter k
        diminuer_cb: fonction pour diminuer k
        get_lbl_text: fonction qui retourne le texte affiché du label
        set_lbl_k_cb: fonction pour enregistrer le label de k
    """
    frame_pm = tk.Frame(frame, bg="#f0f0f0")
    frame_pm.pack(pady=10)

    btn_plus = tk.Button(frame_pm, text="+", command=augmenter_cb)
    btn_plus.pack(side=tk.RIGHT, padx=5)

    lbl_k = tk.Label(frame_pm, text=get_lbl_text(), bg="#f0f0f0")
    lbl_k.pack(side=tk.RIGHT)

    set_lbl_k_cb(lbl_k)

    btn_moins = tk.Button(frame_pm, text="-", command=diminuer_cb)
    btn_moins.pack(side=tk.RIGHT, padx=5)