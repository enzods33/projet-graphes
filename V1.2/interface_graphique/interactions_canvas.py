import tkinter as tk
import utils.fonction_math as fm
import interface_graphique.menu as igm

sommets = []
canva = None
point_deplace = None
derniere_pos_souris = None
click_start_time = None
click_start_pos = None

callback_click = None
callback_reset = None
callback_update_edges = None

def set_canvas(canvas):
    global canva
    canva = canvas

def reset():
    global sommets
    sommets.clear()
    if canva:
        canva.delete("all")
    if callback_reset:
        callback_reset()

def enregistrer_callback_click(func):
    global callback_click
    callback_click = func

def enregistrer_callback_reset(func):
    global callback_reset
    callback_reset = func

def enregistrer_callback_update_edges(func):
    global callback_update_edges
    callback_update_edges = func

def create_point(x, y):
    return canva.create_rectangle(x-3, y-3, x+3, y+3, fill="yellow")

def on_right_click(event):
    click_coords = (event.x, event.y)
    target = fm.find_closest_point(click_coords, sommets, canva.coords)
    if target is not None:
        remove_edges(target)
        canva.delete(target)
        sommets.remove(target)

def remove_edges(sommet):
    point_coords = canva.coords(sommet)
    items = canva.find_all()
    for item in items:
        if canva.type(item) == "line" and fm.is_connected(canva.coords(item), point_coords):
            canva.delete(item)

def is_drag(event):
    for point in sommets:
        x1, y1, x2, y2 = canva.coords(point)
        if x1 <= event.x <= x2 and y1 <= event.y <= y2:
            on_drag_start(event, point)

    if point_deplace==None:
        if callback_click:
                callback_click(event)
        if callback_update_edges:
                callback_update_edges()

        
def on_drag_start(event, point):
    global point_deplace, derniere_pos_souris
    point_deplace = point
    derniere_pos_souris = (event.x, event.y) 

def on_drag_motion(event):
    global point_deplace, derniere_pos_souris
    if point_deplace is not None:
        dx = event.x - derniere_pos_souris[0]
        dy = event.y - derniere_pos_souris[1]
        canva.move(point_deplace, dx, dy)
        derniere_pos_souris = (event.x, event.y)
        if callback_update_edges:
            callback_update_edges()

def on_drag_end(event):
    global point_deplace
    if point_deplace is not None:
        point_deplace = None

def changer_graphe(frame_actuel, root):
    reset()  # Réinitialisation générique
    if callback_reset:
        callback_reset()  # Reset spécifique au graphe (ex: remettre le rayon)
    frame_actuel.destroy()

    igm.ouvrir_menu(root)

def add_button_change_graph(frame, root):
    btn_changer = tk.Button(frame, text="Changer de graphe", command=lambda: changer_graphe(frame, root))
    btn_changer.pack(pady=10)