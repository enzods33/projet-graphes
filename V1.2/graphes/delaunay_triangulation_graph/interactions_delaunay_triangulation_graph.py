# Interactions pour le graphe delaunay_triangulation_graph


import math
from interface_graphique.interactions_canvas import  sommets, canva
from outils_canva import geometrie as geo



def center_of_circle(p1, p2, p3):
    """
    cette fonction permet de déterminer les coordonnées du centre du cercle passant par les trois points du triangle étudié, p1, p2 et p3
    toutes les formules utilisées sont issues d'un cours de 2005 de l'université de Claude Bernard à Lyon
    Paramètres:
        p1, p2, p3 : les couples de coordonées des 3 points du triagnle étudié
    Retour:
        coords_center: couple des coordonnées du centre du cercle

    """
    if not all(isinstance(p, tuple) and len(p) == 2 for p in [p1, p2, p3]):
        raise ValueError("Les points doivent être des tuples de coordonnées (x, y).")


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

def is_connected(sommet1, sommet2):
    """
    Détermine si l'arête entre p1 et p2 doit exister dans la triangulation de Delaunay
    On teste si pour un point p3, le cercle passant par (p1, p2, p3) ne contient aucun autre point.
    Paramètres :
        p1, p2 : couples de coordonnées des deux sommets de l'arête testée
    Retour :
        True si on doit construire une arete dans la triangulation de Delaunay, False sinon.
    """
    if sommet1 is None or sommet2 is None:
        return False 
    p1 = geo.get_center(canva.coords(sommet1))
    p2 = geo.get_center(canva.coords(sommet2))
    sommets_coord = [geo.get_center(canva.coords(s)) for s in sommets]    
    print(sommets)
    for p3 in sommets_coord:
        if p3 == p1 or p3 == p2:        # on passe le tour si p3 est en fait p1 ou p2
            continue 
        
        center = center_of_circle(p1, p2, p3)
        if center is None:              # si les points sont alignés
            continue  

        radius = radius_of_circle(center, p1)

        for p in sommets_coord:
            if p in (p1, p2, p3):       # on ignore si p fait parti des sommets du triangle car ils sont sur le cercle
                continue
            
            dist = math.dist(center, p)
            if dist < radius - 1e-10:   # point strictement à l'intérieur (avec imprécision)
                return False

    return True



def get_graph_type():
    """
    Retourne le type du graphe actuellement utilisé ("Delaunay triangulation graph").
    """
    return "Delaunay triangulation graph"