import tkinter as tk
from interface_graphique import interactions_canvas as ic
from graphes.unit_disk_graph import interactions_UDG as i_udg
from interface_graphique.menu_fichier import ajouter_menu_fichier

def ouvrir_canvas_UDG(root, points=None):
    """
    Ouvre l'interface du graphe de proximité (UDG).
    """
    frame_principal = tk.Frame(root)
    frame_principal.pack(fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(frame_principal, width=600, height=600, background="white")
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    canvas.focus_set()

    ic.set_canvas(canvas)
    ic.enregistrer_callback_click(i_udg.left_click)
    ic.enregistrer_callback_reset(i_udg.reset_specifique)
    ic.enregistrer_callback_update_edges(i_udg.reafficher_les_arêtes)
    ajouter_menu_fichier(root)

    frame_boutons = tk.Frame(frame_principal, bg="#f0f0f0")
    frame_boutons.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.Y)
    i_udg.add_controls(frame_boutons)
    ic.add_button_change_graph(frame_boutons, root)

    if points:
        for x, y in points:
            point = ic.create_point(x, y)
            ic.sommets.append(point)
        if ic.callback_update_edges:
            ic.callback_update_edges()

    canvas.bind("<Button-1>", ic.is_drag)               #clic gauche, va verifier si clic simple ou prolongé
    canvas.bind("<Button-3>", ic.on_right_click)        #clic droit, supression
    canvas.bind("<B1-Motion>", ic.on_drag_motion)       #déplacement
    canvas.bind("<ButtonRelease-1>", ic.on_drag_end)    #relache du clic gauche, ajoute un point si ce n'était qu'un clic
    canvas.bind("<Shift-=>", i_udg.augmenter_rayon)     #le + du clavier principal
    canvas.bind("<Key-+>", i_udg.augmenter_rayon)       #le + du pavé numérique
    canvas.bind("<minus>", i_udg.diminuer_rayon)        #le - du clavier principal
    canvas.bind("<Key-->", i_udg.diminuer_rayon)        #le - du pavé numérique