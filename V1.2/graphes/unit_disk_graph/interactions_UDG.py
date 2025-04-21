import interface_graphique.interactions_canvas as ic
import utils.fonction_math as fm
import tkinter as tk

rayon = 100
lbl_rayon = None

def left_click(event):
    global rayon
    point = ic.create_point(event.x, event.y)
    create_edges(point, rayon)
    ic.sommets.append(point)

def create_edges(new_point, rayon):
    new_coords = ic.canva.coords(new_point)
    new_center = fm.get_center(new_coords)
    nearby_points = fm.find_nearby_points(new_center, ic.sommets, ic.canva.coords, rayon)

    for som in nearby_points:
        som_coords = ic.canva.coords(som)
        som_center = fm.get_center(som_coords)
        ic.canva.create_line(new_center[0], new_center[1], som_center[0], som_center[1], fill="yellow", width=2)

def reafficher_les_arêtes():
    global rayon
    for item in ic.canva.find_all():
        if ic.canva.type(item) == "line":
            ic.canva.delete(item)

    for point in ic.sommets:
        create_edges(point, rayon)

def augmenter_rayon(event=None):
    global rayon
    rayon += 10
    maj_label()
    reafficher_les_arêtes()

def diminuer_rayon(event=None):
    global rayon
    if rayon > 10:
        rayon -= 10
        maj_label()
        reafficher_les_arêtes()

def maj_label():
    if lbl_rayon:
        lbl_rayon.config(text=f"Rayon : {rayon}")

def reset_specifique():
    global rayon
    rayon = 100
    maj_label()

def add_controls(frame):
    global lbl_rayon
    # Boutons +/-
    frame_pm = tk.Frame(frame, bg="#f0f0f0")
    frame_pm.pack(pady=10)

    btn_plus = tk.Button(frame_pm, text="+", command=augmenter_rayon)
    btn_plus.pack(side=tk.RIGHT, padx=5)

    lbl_rayon = tk.Label(frame_pm, text=f"Rayon : {rayon}", bg="#f0f0f0")
    lbl_rayon.pack(side=tk.RIGHT)

    btn_moins = tk.Button(frame_pm, text="-", command=diminuer_rayon)
    btn_moins.pack(side=tk.RIGHT, padx=5)

    # Bouton reset
    btn_reset = tk.Button(frame, text="Reset", command=lambda: [ic.reset(), reset_specifique()])
    btn_reset.pack(pady=10)