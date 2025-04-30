import math

import outils_canva.geometrie as geo
import interface_graphique.interactions_canvas as ic


def is_connected(point1, point2):
    center1 = geo.get_center(ic.canva.coords(point1))
    center2 = geo.get_center(ic.canva.coords(point2))

    disk_radius_canvas = math.dist(center1, center2) / 2
    disk_radius_real = disk_radius_canvas / ic.facteur_global

    disk_center = ((center1[0] + center2[0]) / 2, (center1[1] + center2[1]) / 2)

    for point_i in ic.sommets:
        if point_i not in (point1, point2):
            centeri = geo.get_center(ic.canva.coords(point_i))
            distance_canvas = math.dist(centeri, disk_center)
            distance_real = distance_canvas / ic.facteur_global

            if distance_real < disk_radius_real:
                return False

    return True
        
def get_graph_type():
    """
    Retourne le type du graphe actuellement utilisé ("Integer graph").
    """
    return "Gabriel graph"