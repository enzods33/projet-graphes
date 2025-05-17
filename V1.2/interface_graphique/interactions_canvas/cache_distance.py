"""
Module cache_distance.py

Gestion du cache des distances entre les sommets, pour accélérer les calculs et éviter les calculs inutiles.
"""

import math
import interface_graphique.interactions_canvas.sommets as sommets

distance_cache = {}
_all_edges_cache = {
    "edges": [],
    "positions": [],
    "count": 0
}

def get_real_distance(idx1, idx2):
    """Renvoie la distance réelle entre deux sommets en utilisant un cache."""
    key = tuple(sorted((idx1, idx2)))

    if key not in distance_cache:
        (x1, y1) = sommets.points[idx1]
        (x2, y2) = sommets.points[idx2]
        dist = math.dist((x1, y1), (x2, y2))
        distance_cache[key] = dist

    return distance_cache[key]

def add_to_cache(nouveau_point):
    """Calcule et ajoute toutes les distances entre un nouveau point et les autres dans le cache."""
    for elements_differents in range(len(sommets.points)):
        if elements_differents != nouveau_point:
            get_real_distance(nouveau_point, elements_differents)

def remove_edges(idx_to_remove):
    """Supprime toutes les distances liées à un sommet supprimé dans le cache."""
    global distance_cache
    new_cache = {}
    for (i, j), dist in distance_cache.items():
        if i != idx_to_remove and j != idx_to_remove:
            ni = i - 1 if i > idx_to_remove else i      #on réactualise les indices de tous les autres élements du dictionnaire
            nj = j - 1 if j > idx_to_remove else j
            new_cache[(ni, nj)] = dist
    distance_cache = new_cache

def get_all_edges():
    """
    Retourne toutes les arêtes avec leur distance.
    Ne recalcule que si les positions des sommets ont changé.
    """
    points = sommets.points

    if (len(points) != _all_edges_cache["count"]or _all_edges_cache["positions"] != points):
        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = get_real_distance(i, j)
                edges.append((dist, i, j))

        _all_edges_cache["edges"] = edges
        _all_edges_cache["positions"] = list(points)
        _all_edges_cache["count"] = len(points)

    return _all_edges_cache["edges"]

def refresh_point_distances(idx):
    """
    Supprime puis régénère toutes les distances liées au point d'indice idx dans le cache.
    """
    global distance_cache
    keys_to_delete = [key for key in distance_cache if idx in key]
    for key in keys_to_delete:
        del distance_cache[key]

    add_to_cache(idx)