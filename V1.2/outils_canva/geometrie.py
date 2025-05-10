"""
Module contenant des fonctions utiles pour les opérations géométriques 
liées aux sommets et arêtes dans les graphes.
"""
import math

def get_center(coords):
    """
    Calcule les coordonnées du centre d'un rectangle à partir de ses coins.

    Paramètres :
        coords : liste ou tuple contenant [x1, y1, x2, y2], 
                 les coordonnées des coins opposés du rectangle.

    retour :
        Tuple (x, y) représentant le centre du rectangle.

    >>> get_center([0, 0, 10, 10])
    (5.0, 5.0)
    >>> get_center([2, 4, 6, 8])
    (4.0, 6.0)
    >>> get_center([-10, -10, 10, 10])
    (0.0, 0.0)
    >>> get_center((0, 0, 0, 0))
    (0.0, 0.0)
    >>> get_center([1.5, 2.5, 3.5, 4.5])
    (2.5, 3.5)

    """
    return ( (coords[0] + coords[2]) / 2, (coords[1] + coords[3]) / 2 )

def find_nearby_points(new_point, sommets, coords_func, rayon):
    """
    Retourne la liste des sommets situés à une distance du point donné inférieure ou égale au rayon

    Paramètres :
        new_point : tuple (x, y), coordonnées du point ajouté
        sommets : liste d'objets ( des Tkinter ID ) représentant les sommets existants
        coords_func : fonction prenant un sommet et retournant ses coordonnées
        rayon : distance maximale pour connecter deux points

    Retour :
        Liste des sommets à relier au nouveau point.
    """
    nearby = []
    for som in sommets:
        center = get_center(coords_func(som))
        if math.dist(center, new_point) <= rayon:
            nearby.append(som)
    return nearby

def find_click_point(click_point, sommets, min_dist):
    """
    Trouve l'index du sommet le plus proche d'un point cliqué, si la distance est inférieure à un seuil.

    Paramètres :
        click_point : tuple (x, y), coordonnées du clic.
        sommets : liste de tuples (x, y).
        min_dist : distance seuil.

    Retour :
        Index du sommet le plus proche, ou None.
    """
    closest_idx = None
    closest_dist = min_dist

    for idx, (x, y) in enumerate(sommets):
        dist = math.dist(click_point, (x, y))
        if dist < closest_dist:
            closest_idx = idx
            closest_dist = dist

    return closest_idx

def is_connected(line_coords, point_coords):
    """
    Vérifie si une arete est connectée à un sommet donné.
    Deux extrémités de la ligne sont comparées au centre du point.

    Paramètres :
        line_coords : liste [x1, y1, x2, y2], coordonnées de la ligne.
        point_coords : liste [x1, y1, x2, y2], coordonnées du point (rectangle).

    Retour :
        True si le point est connecté à l'une des extrémités de la ligne, False sinon.
    """
    px, py = get_center(point_coords)
    return (line_coords[0], line_coords[1]) == (px, py) or (line_coords[2], line_coords[3]) == (px, py)
