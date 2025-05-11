# Interactions pour le graphe delaunay_triangulation_graph

import math
from interface_graphique import interactions_canvas as ic
from outils_canva import geometrie as geo

def is_connected(idx1, idx2):
    """
    Détermine si l'arête entre idx1 et idx2 doit exister dans la triangulation de Delaunay.
    Une arête fait partie de la triangulation de Delaunay s'il existe un cercle passant par 
    ses extrémités ne contenant aucun autre point du graphe.
    """

    sommets_coord = ic.sommets.copy()

    p1 = sommets_coord[idx1]
    p2 = sommets_coord[idx2]

    if len(sommets_coord) <= 3:
        return True

    for idx3, p3 in enumerate(sommets_coord):
        if idx3 in (idx1, idx2):
            continue
        
        center = geo.center_of_circle(p1, p2, p3)
        if center is None:
            continue
        
        radius = geo.radius_of_circle(center, p1)

        cercle_vide = True  # Ici on teste cercle par cercle

        for idx, p in enumerate(sommets_coord):
            if idx in (idx1, idx2, idx3):
                continue

            dist = math.dist(center, p)
            if dist < radius - 1e-10:
                cercle_vide = False
                break

        if cercle_vide:
            # Si on trouve un cercle vide, l'arête est valide
            return True

    # Aucun cercle vide trouvé ➔ l'arête n'est pas valide
    return False


def get_graph_type():
    """
    Retourne le type du graphe actuellement utilisé ("Delaunay triangulation graph").
    """
    return "Delaunay triangulation graph"