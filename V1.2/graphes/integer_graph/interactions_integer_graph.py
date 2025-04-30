import math

import outils_canva.geometrie as geo
from interface_graphique import interactions_canvas as ic

def is_connected(point1, point2, epsilon=1e-3):
    p1 = geo.get_center(ic.canva.coords(point1))
    p2 = geo.get_center(ic.canva.coords(point2))

    if p1 is None or p2 is None:
        return False

    distance = math.dist(p1, p2)
    distance_reelle = distance / ic.facteur_global

    # Vérifier que la distance est "très proche" d'un entier
    return abs(distance_reelle - round(distance_reelle)) <= epsilon

def get_graph_type():
    """
    Retourne le type du graphe actuellement utilisé ("Integer graph").
    """
    return "Integer graph"

