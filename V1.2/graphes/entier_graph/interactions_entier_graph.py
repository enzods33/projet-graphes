import math

import outils_canva.geometrie as geo
from interface_graphique import interactions_canvas as ic

def is_connected(point1, point2):
    p1 = ic.coordonnees_reelles.get(point1)
    p2 = ic.coordonnees_reelles.get(point2)

    if p1 is None or p2 is None:
        return False

    distance = math.dist(p1, p2)
    return distance.is_integer()

def get_type_graphe():
    """
    Retourne le type du graphe actuellement utilisé ("Entier graph").
    """
    return "Entier graph"
