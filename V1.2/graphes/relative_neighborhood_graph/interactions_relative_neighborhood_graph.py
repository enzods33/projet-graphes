# Interactions pour le graphe relative_neighborhood_graph
import tkinter as tk
from interface_graphique import interactions_canvas as ic

def is_connected(idx1, idx2):
    """
    Détermine si p1 et p2 doivent être connectés
    """
    distance_p1_p2 = ic.get_real_distance(idx1, idx2)

    for idx_r in range(len(ic.sommets)):
        if idx_r != idx1 and idx_r != idx2:
            if max(ic.get_real_distance(idx1, idx_r), ic.get_real_distance(idx2, idx_r)) < distance_p1_p2:
                return False
    return True
    


def get_graph_type():
    """
    Retourne le type du graphe actuellement utilisé ("Relative neighborhood graph").
    """
    return "Relative neighborhood graph"