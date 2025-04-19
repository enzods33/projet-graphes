import math

def get_center(coords):
    """renvoie les coordonnées du centre d'un rectangle donné par ses coins"""
    return ( (coords[0] + coords[2]) / 2, (coords[1] + coords[3]) / 2 )

def find_nearby_points(new_point, sommets, coords_func, rayon):
    """
    retourne la liste des sommets à relier au nouveau point s'ils sont à une distance <= rayon
    coords_func : fonction renvoyant les coordonnées d'un point
    """
    nearby = []
    for som in sommets:
        center = get_center(coords_func(som))
        if math.dist(center, new_point) <= rayon:
            nearby.append(som)
    return nearby

def find_closest_point(click_point, sommets, coords_func):
    """
    trouve le sommet le plus proche d'un point donné, si distance < min.
    retourne le sommet ou rien
    """
    min = 10
    closest = None
    for som in sommets:
        center = get_center(coords_func(som))
        dist = math.dist(center, click_point)
        if dist < min:
            min = dist
            closest = som
    return closest

def is_connected(line_coords, point_coords):
    """
    vérifie si une ligne est connectée à un sommet de coordonnées "point_coords"
    """
    px, py = get_center(point_coords)
    return (line_coords[0], line_coords[1]) == (px, py) or (line_coords[2], line_coords[3]) == (px, py)

def couples_som():
    """
    renvoie une liste de couple de sommets reliés    """
    pass