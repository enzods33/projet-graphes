import math

import outils_canva.geometrie as geo
from interface_graphique import interactions_canvas as ic

def is_connected(idx1, idx2):
    p1 = ic.sommets[idx1]
    p2 = ic.sommets[idx2]

    distance = math.dist(p1, p2)

    # Vérifier que la distance est "très proche" d'un entier
    return abs(distance - round(distance)) <= 1e-3

def get_graph_type():
    """
    Retourne le type du graphe actuellement utilisé ("Integer graph").
    """
    return "Integer graph"

