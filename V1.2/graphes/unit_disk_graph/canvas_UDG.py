import tkinter as tk
from interface_graphique import interactions_canvas as ic
from graphes.unit_disk_graph import interactions_UDG as i_udg
from interface_graphique.menu_fichier import ajouter_menu_fichier

def ouvrir_canvas_UDG(root, points=None):
    """
    Ouvre l'interface du graphe de proximité (UDG).
    """
    ic.reset()

    frame_principal = tk.Frame(root)
    frame_principal.pack(fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(frame_principal, width=600, height=600, background="white")
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    ic.set_canvas(canvas)
    ajouter_menu_fichier(root)

    distance = 100
    ic.enregistrer_fonction_rafraichissement_arêtes(lambda: i_udg.reafficher_les_arêtes(distance))
    ic.add_button_change_graph(frame_principal, root)

    if points:
        for x, y in points:
            point = ic.create_point(x, y)
            ic.sommets.append(point)
        if ic.edge_update_function:
            ic.edge_update_function()

    canvas.bind("<Button-1>", lambda event: i_udg.left_click(event, distance))
    canvas.bind("<Button-3>", ic.on_right_click)
    canvas.bind("<ButtonPress-2>", ic.on_drag_start)
    canvas.bind("<B2-Motion>", ic.on_drag_motion)
    canvas.bind("<ButtonRelease-2>", ic.on_drag_end)