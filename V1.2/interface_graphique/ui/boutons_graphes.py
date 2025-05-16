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

def add_common_buttons(frame, root):
    """
    Fonction qui ajoute les boutons communs à tous les graphes
    """

    frame_zoom = tk.Frame(frame, bg="#f0f0f0")
    frame_zoom.pack(pady=10)
    tk.Button(frame_zoom, text="Zoom +", command=ic.zoom_in).pack(side=tk.LEFT)
    tk.Button(frame_zoom, text="Zoom -", command=ic.zoom_out).pack(side=tk.LEFT)

    label_zoom = tk.Label(frame, text="Zoom : x1.00", bg="#f0f0f0")
    label_zoom.pack(pady=5)
    ic.set_zoom_label(label_zoom)

    tk.Button(frame, text="Full reset view", command=ic.full_reset_view).pack(pady=10)

    label_compteur = tk.Label(frame, text="Sommets : 0\nArêtes : 0", bg="#f0f0f0")
    label_compteur.pack(pady=10)
    ic.set_counter_label(label_compteur)   

    tk.Button(frame, text="Reset", command=ic.reset).pack(pady=10)

    btn_changer = tk.Button(frame, text="Changer de graphe", command=lambda: ic.change_graph(root))
    btn_changer.pack(pady=20)

def add_plus_minus_buttons(frame, augmenter_cb, diminuer_cb, get_lbl_text, set_lbl_cb):
    """
    Fonction qui ajoute les boutons + et -, et défini le label du parametre
    qui pourra etre modifié.
    """

    frame_plus_minus_buttons = tk.Frame(frame, bg="#f0f0f0")
    frame_plus_minus_buttons.pack(pady=10)

    btn_plus = tk.Button(frame_plus_minus_buttons, text="+", command=augmenter_cb)
    btn_plus.pack(side=tk.RIGHT)

    lbl_k = tk.Label(frame_plus_minus_buttons, text=get_lbl_text(), bg="#f0f0f0")
    lbl_k.pack(side=tk.RIGHT)

    set_lbl_cb(lbl_k)

    btn_moins = tk.Button(frame_plus_minus_buttons, text="-", command=diminuer_cb)
    btn_moins.pack(side=tk.RIGHT)