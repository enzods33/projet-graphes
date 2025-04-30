# Interactions pour le graphe relative_neighborhood_graph
import tkinter as tk
from interface_graphique import interactions_canvas as ic

def is_connected(p1, p2):
    """
    Détermine si p1 et p2 doivent être connectés
    """
    distance_p1_p2 = ic.get_real_distance(p1, p2)
    for r in ic.sommets:
        if r != p1 and r != p2:
            if max(ic.get_real_distance(p1, r), ic.get_real_distance(p2, r)) <distance_p1_p2:
                return False
    return True
    


def get_type_graphe():
    """
    Retourne le type du graphe actuellement utilisé ("Relative neighborhood graph").
    """
    return "Relative neighborhood graph"