import tkinter as tk

sommets = []
canva = None
edge_update_function = None
point_deplace = None
derniere_pos_souris = None

def set_canvas(canvas):
    """Associe le canvas global pour les interactions."""
    global canva
    canva = canvas

def reset():
    """Réinitialise les sommets et le canvas."""
    global sommets, canva
    sommets.clear()

def create_point(x, y):
    return canva.create_rectangle(x-3, y-3, x+3, y+3, fill="yellow")

def on_right_click(event):
    from utils.fonction_math import find_closest_point, is_connected
    min_distance = 10
    click_coords = (event.x, event.y)
    target = find_closest_point(click_coords, sommets, canva.coords)
    if target is not None:
        remove_edges(target)
        canva.delete(target)
        sommets.remove(target)

def remove_edges(sommet):
    from utils.fonction_math import is_connected
    point_coords = canva.coords(sommet)
    items = canva.find_all()
    for item in items:
        if canva.type(item) == "line":
            if is_connected(canva.coords(item), point_coords):
                canva.delete(item)

def on_drag_start(event):
    global point_deplace, derniere_pos_souris
    for point in sommets:
        x1, y1, x2, y2 = canva.coords(point)
        if x1 <= event.x <= x2 and y1 <= event.y <= y2:
            point_deplace = point
            derniere_pos_souris = (event.x, event.y)

def on_drag_motion(event):
    global point_deplace, derniere_pos_souris
    if point_deplace is not None:
        dx = event.x - derniere_pos_souris[0]
        dy = event.y - derniere_pos_souris[1]
        canva.move(point_deplace, dx, dy)
        derniere_pos_souris = (event.x, event.y)
        if edge_update_function:
            edge_update_function()

def on_drag_end(event):
    global point_deplace
    point_deplace = None

def enregistrer_fonction_rafraichissement_arêtes(fonction):
    global edge_update_function
    edge_update_function = fonction

def add_button_change_graph(frame, root):
    from interface_graphique.menu import ouvrir_menu
    frame_boutons = tk.Frame(frame)
    frame_boutons.pack(side=tk.RIGHT, fill=tk.Y)

    btn_changer = tk.Button(frame_boutons, text="Changer de graphe", command=lambda: changer_graphe(frame, root))
    btn_changer.pack(padx=10, pady=10)

def changer_graphe(frame_actuel, root):
    reset()
    frame_actuel.destroy()
    from interface_graphique.menu import ouvrir_menu
    ouvrir_menu(root)