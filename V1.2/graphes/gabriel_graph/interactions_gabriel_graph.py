import math

import outils_canva.geometrie as geo
import interface_graphique.interactions_canvas as ic


def is_connected(idx1, idx2):
    """
    Deux sommets sont connectés s'il n'existe aucun autre sommet à l'intérieur
    du cercle dont ils forment le diamètre (Gabriel Graph).
    """

    if idx1 >= len(ic.sommets) or idx2 >= len(ic.sommets):
        return False

    p1 = ic.sommets[idx1]
    p2 = ic.sommets[idx2]

    if p1 == p2:
        return False

    # Centre du cercle
    disk_center = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
    disk_radius = math.dist(p1, p2) / 2

    for idx, p in enumerate(ic.sommets):
        if idx in (idx1, idx2):
            continue

        distance = math.dist(p, disk_center)
        if distance < disk_radius - 1e-10:
            return False

    return True
        
def get_graph_type():
    """
    Retourne le type du graphe actuellement utilisé ("Integer graph").
    """
    return "Gabriel graph"