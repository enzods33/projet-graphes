# Interactions pour le graphe nearest_neighbor_graph
import tkinter as tk
from interface_graphique import interactions_canvas as ic


def trouver_voisin_le_plus_proche(point, sommets):
    """
    Trouve le plus proche voisin du point donné parmi les autres sommets.
    """
    dists = [
        (p, ic.get_distance_reelle(point, p))
        for p in sommets if p != point
    ]
    if not dists:
        return None
    voisin, distance_p_point = min(dists, key=lambda x: x[1])
    return voisin

def is_connected(p1, p2):
    """
    Détermine si p1 et p2 doivent être connectés 
    """
    voisin1 = trouver_voisin_le_plus_proche(p1, ic.sommets)
    if voisin1 == p2:
        return True

    voisin2 = trouver_voisin_le_plus_proche(p2, ic.sommets)
    return voisin2 == p1


def get_type_graphe():
    """
    Retourne le type du graphe actuellement utilisé ("nearest neighbor graph").
    """
    return "Nearest neighbor graph"