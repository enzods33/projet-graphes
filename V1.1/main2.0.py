import tkinter as tk
import fonction_math as fm

def create_point(x, y):
    """
    crée un carré de 6 par 6 aux coordonnées (x,y)
    """
    return canva.create_rectangle(x-3, y-3, x+3, y+3, fill="yellow")

def create_edges(new_point, rayon: int):
    """
    crée une arête entre le nouveau point (new_point) et tous les points situés à une distance inférieure à rayon
    """
    new_coords = canva.coords(new_point)
    new_center = fm.get_center(new_coords)
    nearby_points = fm.find_nearby_points(new_center, sommets, canva.coords, rayon)

    for som in nearby_points:
        som_coords = canva.coords(som)
        som_center = fm.get_center(som_coords)
        canva.create_line(new_center[0], new_center[1], som_center[0], som_center[1], fill="yellow", width=2)

def left_click(event):
    """
    affiche le nouveau point au coordonnées du clique gauche, et le relie aux points qui sont à une distance inférieure à "distance"
    """
    point = create_point(event.x, event.y)
    create_edges(point, distance)
    sommets.append(point)

def on_right_click(event):
    """
    retire le  point au coordonnées du clique droit et les arêtes reliées à ce point
    """
    min=10
    click_coords = (event.x, event.y)
    target = fm.find_closest_point(click_coords, sommets, canva.coords)

    if target is not None:
        remove_edges(target)
        canva.delete(target)
        sommets.remove(target)

def remove_edges(sommet):
    """
    retire les arêtes qui sont connéctées au sommet"""
    point_coords = canva.coords(sommet)
    items = canva.find_all()
    for item in items:
        if canva.type(item) == "line":
            if fm.is_connected(canva.coords(item), point_coords):
                canva.delete(item)



root = tk.Tk()
root.title("Graphe")
root.geometry("600x400")

sommets = []

distance = 100

# Création d'un panneau (Frame) pour contenir les boutons et la zone de texte
button_frame = tk.Frame(root, background="#7ed8f3")
button_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Création du canvas qui prendra la place restante à gauche
canva = tk.Canvas(root, width=600, height=400, background="white")
canva.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Petit cadre pour le contrôle du rayon
rayon_frame = tk.Frame(button_frame, background="#7ed8f3")
rayon_frame.pack(pady=20)

# Bouton "moins"
btn_minus = tk.Button(rayon_frame, text=" - ")
btn_minus.pack(side=tk.LEFT, padx=5)

# Zone d'affichage de la valeur du rayon (on préfère un Entry pour une valeur simple)
rayon_value = tk.StringVar(value="10")  # Valeur initiale
entry_rayon = tk.Entry(rayon_frame, textvariable=rayon_value, width=5, justify='center')
entry_rayon.pack(side=tk.LEFT, padx=5)

# Bouton "plus"
btn_plus = tk.Button(rayon_frame, text=" + ")
btn_plus.pack(side=tk.LEFT, padx=5)


canva.bind("<Button-1>", left_click)  # Clic gauche : ajoute un sommet
canva.bind("<Button-3>", on_right_click)  # Clic droit : supprime sommet et arêtes

root.mainloop()