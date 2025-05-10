# Interactions pour le graphe delaunay_triangulation_graph

import math
from interface_graphique import interactions_canvas as ic


def center_of_circle(p1, p2, p3):
    """
    cette fonction permet de déterminer les coordonnées du centre du cercle passant par les trois points du triangle étudié, p1, p2 et p3
    toutes les formules utilisées sont issues d'un cours de 2005 de l'université de Claude Bernard à Lyon
    Paramètres:
        p1, p2, p3 : les couples de coordonées des 3 points du triagnle étudié
    Retour:
        coords_center: couple des coordonnées du centre du cercle

    """
    (x1, y1) = p1
    (x2, y2) = p2
    (x3, y3) = p3

    #vérifiaction que les points ne sont pas alignés à l'aide du déterminant:
    det = (x2 - x1)*(y3 - y2) - (x3 - x2)*(y2 - y1)
    if det == 0:            # Points alignés
        return None  

    # Calcul des milieus des segments p1p2 et p2p3:
    # Milieu du segment p1p2
    middle_x_p1p2 = (x1 + x2) / 2
    middle_y_p1p2 = (y1 + y2) / 2  
    # Milieu du segment p2p3
    middle_x_p2p3 = (x2 + x3) / 2
    middle_y_p2p3 = (y2 + y3) / 2  
    
    # Calcul des pentes des médiatrices
    # Pente de la médiatrice de p1p2 : a1 = -(x2 - x1) / (y2 - y1)
    # La pente de la médiatrice est l'inverse négatif de la pente du segment p1p2
    if y2 - y1 == 0:  # p1p2 horizontale (de plus division par 0 interdite)
        a1 = 0
    else:
        a1 = -(x2 - x1) / (y2 - y1)
    
    # Pente de la médiatrice de P2P3 : a2 = -(x3 - x2) / (y3 - y2)
    if y3 - y2 == 0:  #  p2p3 horizontale (de plus division par 0 interdite)
        a2 = 0
    else:
        a2 = -(x3 - x2) / (y3 - y2)
    
    # Calcul des ordonnées à l'origine b1 et b2 
    #( y=ax+b <=> b=y-ax )
    b1 = middle_y_p1p2 - a1 * middle_x_p1p2
    b2 = middle_y_p2p3 - a2 * middle_x_p2p3
    
    # Résolution du système d'équations des médiatrices pour trouver l'intersection
    # Equation 1: y = a1 * x + b1
    # Equation 2: y = a2 * x + b2
    if a1 == a2:  # les médiatrices sont paralleles 
        return None
    
    # Résolution des équations pour x et y
    x_center = (b2 - b1) / (a1 - a2)
    y_center = a1 * x_center + b1
    coords_center = (x_center, y_center)

    return coords_center

def radius_of_circle(coords, p):
    """
    cette fonction renvoie le rayon du cercle passant par les sommets du triangle étudié
    tirée du même cours de l'université de Claude Bernard que la fonction center_of_circle
    paramètres:
        coords: le couple de coordonnées du centre du cerlce
        p: le couple de coordonées d'un sommet du triangle
    retour:
        radius: le rayon du cercle
    """
    (x1, y1) = p
    (x_center, y_center) = coords
    radius = math.sqrt((x_center - x1)**2 + (y_center - y1)**2)
    return radius

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
        
        center = center_of_circle(p1, p2, p3)
        if center is None:
            continue
        
        radius = radius_of_circle(center, p1)

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