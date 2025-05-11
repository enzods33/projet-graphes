import math
from interface_graphique import interactions_canvas as ic
from outils_canva import geometrie as geo
from graphes.delaunay_triangulation_graph import interactions_delaunay_triangulation_graph as i_dtg

# Variables globales
urquhart_edges = set()
last_n_points = 0
last_positions = []

# Fonctions principales
def is_connected(idx1, idx2):
    """
    Retourne True si idx1 et idx2 sont connectés dans l'Urquhart Graph.
    On part de la triangulation de Delaunay, puis on supprime la plus longue arête de chaque triangle.
    """
    global urquhart_edges, last_n_points, last_positions
    points = ic.sommets

    if len(points) != last_n_points or points != last_positions:
        construire_urquhart()

    edge = tuple(sorted((idx1, idx2)))
    return edge in urquhart_edges

def get_graph_type():
    return "Urquhart Graph"

def reset_specific():
    """Reset les données propres à l'Urquhart graph."""
    global urquhart_edges
    urquhart_edges.clear()

# Construction de l'Urquhart Graph
def construire_urquhart():
    global urquhart_edges, last_n_points, last_positions
    urquhart_edges.clear()

    points = ic.sommets.copy()
    last_positions = points.copy()
    last_n_points = len(points)

    n = len(points)
    if n < 3:
        return

    triangles = []

    for i in range(n):
        for j in range(i+1, n):
            if not i_dtg.is_connected(i, j):
                continue
            for k in range(j+1, n):
                if not (i_dtg.is_connected(i, k) and i_dtg.is_connected(j, k)):
                    continue
                triangles.append((i, j, k))

    for (i, j, k) in triangles:
        d_ij = math.dist(points[i], points[j])
        d_ik = math.dist(points[i], points[k])
        d_jk = math.dist(points[j], points[k])

        longueurs = [(d_ij, (i, j)), (d_ik, (i, k)), (d_jk, (j, k))]
        longueurs.sort()

        urquhart_edges.add(tuple(sorted(longueurs[0][1])))
        urquhart_edges.add(tuple(sorted(longueurs[1][1])))

    ic.update_edge()