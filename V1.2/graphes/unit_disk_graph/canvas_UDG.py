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
    ic.rayon_actuel = 100
    ajouter_menu_fichier(root)

    ic.enregistrer_fonction_rafraichissement_arêtes(lambda: i_udg.reafficher_les_arêtes(ic.rayon_actuel))
    ic.add_button_change_graph(frame_principal, root)

    frame_boutons = tk.Frame(frame_pricipal)
    frame_boutons.pack(side=tk.RIGHT, fill=tk.Y)

    def augmenter_rayon():
        ic.rayon_actuel += 10
        if ic.edge_update_function:                 #si un recalcule des aretes est effectué, alors on appelle la fonction
            ic.edge_update_function()

    def diminuer_rayon():
        if ic.rayon_actuel > 10:                    #on vérifie que le rayon est d'au moins 10 pour ne pas avoir un rayon nul ou négatif
            ic.rayon_actuel -= 10
            if ic.edge_update_function:             #si un recalcule des aretes est effectué, alors on appelle la fonction
                ic.edge_update_function()

    btn_plus = tk.Button(frame_boutons, text= "+", command = augmenter_rayon)
    btn_plus.pack(padx = 10, pady = 5)

    btn_moins = tk.Button(frame_boutons, text = "-", command = diminuer_rayon)
    btn_moins.pack(padx = 10, pady = 5)

    if points:
        for x, y in points:
            point = ic.create_point(x, y)
            ic.sommets.append(point)
        if ic.edge_update_function:
            ic.edge_update_function()

    canvas.bind("<Button-1>", ic.on_drag_start)         #clic gauche, va verifier si clic simple ou prolongé
    canvas.bind("<Button-3>", ic.on_right_click)        #clic droit, supression
    canvas.bind("<B1-Motion>", ic.on_drag_motion)       #déplacement
    canvas.bind("<ButtonRelease-1>", ic.on_drag_end)    #relache du clic gauche, ajoute un point si ce n'était qu'un clic