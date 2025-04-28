"""
Module contenant des fonctions utilitaires pour les opérations géométriques 
liées aux sommets et arêtes dans les graphes.
"""
import math
import random
from outils_canva.constantes import MIN_DIST

def get_center(coords):
    """
    Calcule les coordonnées du centre d'un rectangle à partir de ses coins.

    Paramètres :
        coords : liste ou tuple contenant [x1, y1, x2, y2], 
                 les coordonnées des coins opposés du rectangle.

    Retour :
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
    Retourne la liste des sommets situés à une distance inférieure ou égale au rayon
    à partir du point donné.

    Paramètres :
        new_point : tuple (x, y), coordonnées du point ajouté.
        sommets : liste d'objets (Tkinter IDs) représentant les sommets existants.
        coords_func : fonction prenant un sommet et retournant ses coordonnées.
        rayon : float, distance maximale pour connecter deux points.

    Retour :
        Liste des sommets à relier au nouveau point.
    """
    nearby = []
    for som in sommets:
        center = get_center(coords_func(som))
        if math.dist(center, new_point) <= rayon:
            nearby.append(som)
    return nearby

def find_closest_point(click_point, sommets, coords_func):
    """
    Trouve le sommet le plus proche d'un point cliqué, si la distance est inférieure à un seuil.

    Paramètres :
        click_point : tuple (x, y), coordonnées du clic.
        sommets : liste de sommets (Tkinter IDs).
        coords_func : fonction prenant un sommet et retournant ses coordonnées.

    Retour :
        Le sommet le plus proche, ou None si aucun n'est assez proche.
    """
    closest = None
    for som in sommets:
        center = get_center(coords_func(som))
        dist = math.dist(center, click_point)
        if dist < MIN_DIST:
            MIN_DIST = dist
            closest = som
    return closest

def is_connected(line_coords, point_coords):
    """
    Vérifie si une ligne est connectée à un sommet donné.

    Deux extrémités de la ligne sont comparées au centre du point.

    Paramètres :
        line_coords : liste [x1, y1, x2, y2], coordonnées de la ligne.
        point_coords : liste [x1, y1, x2, y2], coordonnées du point (rectangle).

    Retour :
        True si le point est connecté à l'une des extrémités de la ligne, False sinon.
    """
    px, py = get_center(point_coords)
    return (line_coords[0], line_coords[1]) == (px, py) or (line_coords[2], line_coords[3]) == (px, py)

def generer_nuage_points(xmin, xmax, ymin, ymax, npoints):
    """
    Génère une liste de points aléatoires dans les intervalles donnés.

    Retour :
        Liste de tuples (x, y)
    """
    points = []
    for _ in range(npoints):
        x = random.uniform(xmin, xmax) #et pas randint pour accepter les nombres a virgule
        y = random.uniform(ymin, ymax)
        points.append((x, y))
    return points

