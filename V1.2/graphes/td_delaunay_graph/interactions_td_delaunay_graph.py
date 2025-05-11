# Interactions pour le graphe TD-Delaunay
# interactions_td_delaunay_graph.py
"""
Interactions pour le TD-Delaunay Graph (basé sur la triangular distance).
"""

from interface_graphique import interactions_canvas as ic
import outils_canva.geometrie as geo  

def get_graph_type():
    """
    Retourne le nom du graphe.
    """
    return "TD Delaunay Graph"

def is_connected(idx1, idx2):
    """
    Détermine si deux sommets doivent être reliés dans le TD-Delaunay Graph.

    Deux points idx1 et idx2 sont connectés si :
    Il existe un troisième point idx3 tel que
    le triangle équilatéral centré sur idx3 capture idx1 et idx2
    sans capturer aucun autre point.

    Retourne :
        True si une telle connexion est valide, False sinon.
    """

    sommets = ic.sommets.copy()

    if len(sommets) <= 2:
        return True

    p1 = sommets[idx1]
    p2 = sommets[idx2]

    for idx3, p3 in enumerate(sommets):
        if idx3 in (idx1, idx2):
            continue

        if triangle_captures(p3, p1, p2, sommets, ignore_indices={idx1, idx2, idx3}):
            return True

    return False

def triangle_captures(origin, p1, p2, points, ignore_indices):
    """
    Vérifie si un triangle équilatéral centré sur 'origin' capture 'p1' et 'p2' sans capturer d'autres points.
    """

    dist1 = geo.triangular_distance(origin, p1)
    dist2 = geo.triangular_distance(origin, p2)
    needed_radius = max(dist1, dist2)

    for idx, p in enumerate(points):
        if idx in ignore_indices:
            continue

        if geo.triangular_distance(origin, p) < needed_radius - 1e-10:
            return False  # Un point est capturé par le triangle avant p1 et p2.

    return True