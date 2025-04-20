
import tkinter as tk
import time

sommets = []
canva = None
edge_update_function = None
point_deplace = None
derniere_pos_souris = None
click_start_time = None         #pour enregistrer le moment du clic
click_start_pos = None          #pour enregistrer la position du clic
rayon_actuel = 100

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
    global point_deplace, derniere_pos_souris, click_start_time, click_start_pos
    click_start_time = time.time()
    click_start_pos = (event.x, event.y)
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
    global point_deplace, click_start_time, click_start_pos
    import time
    
    if point_deplace is not None:
        point_deplace = None
        return
    if click_start_time and click_start_pos:
        duration = time.time() - click_start_time
        dx = abs(event.x - click_start_pos[0])      #difference de position x
        dy = abs(event.y - click_start_pos[1])      #difference de position y
        if duration < 0.2 and dx < 5 and dy < 5:    #clic rapide sans mouvement involontaire de la souris
            from graphes.unit_disk_graph import interactions_UDG as i_udg
            rayon = 100
            i_udg.left_click(event, rayon)
    
    click_start_time = None     #on reinitialise 
    click_start_pos = None      #on reinitialise



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