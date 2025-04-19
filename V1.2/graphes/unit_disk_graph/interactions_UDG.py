import interface_graphique.interactions_canvas as ic
import utils.fonction_math as fm

def left_click(event, rayon):
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

def reafficher_les_arêtes(rayon):
    # Supprimer toutes les lignes existantes
    for item in ic.canva.find_all():
        if ic.canva.type(item) == "line":
            ic.canva.delete(item)

    # Recalculer les connexions
    for point in ic.sommets:
        create_edges(point, rayon)  # ou passe le rayon dynamiquement