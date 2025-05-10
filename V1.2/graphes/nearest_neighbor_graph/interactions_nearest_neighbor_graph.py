# Interactions pour le graphe nearest_neighbor_graph
import tkinter as tk
from interface_graphique import interactions_canvas as ic

def find_nearest_neighbor(idx_point, sommets):
    """
    Trouve le plus proche voisin du point donné parmi les autres sommets.
    """
    dists = [
        (idx, ic.get_real_distance(idx_point, idx))
        for idx in range(len(sommets)) if idx != idx_point
    ]
    if not dists:
        return None
    voisin, distance = min(dists, key=lambda x: x[1])
    return voisin

def is_connected(idx1, idx2):
    """
    Détermine si p1 et p2 doivent être connectés 
    Parametres:
        p1: premier sommet
        p2: deuxième sommet
    """
    voisin1 = find_nearest_neighbor(idx1, ic.sommets)
    if voisin1 == idx2:
        return True

    voisin2 = find_nearest_neighbor(idx2, ic.sommets)
    return voisin2 == idx1


def get_graph_type():
    """
    Retourne le type du graphe actuellement utilisé ("nearest neighbor graph").
    """
    return "Nearest neighbor graph"