"""
Module contenant des fonctions utiles pour les opérations géométriques 
liées aux sommets et arêtes dans les graphes.
"""
import math

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

def get_center(coords): 
    """
    Calcule les coordonnées du centre d'un rectangle à partir de ses coins.

    Paramètres :
        coords : liste ou tuple contenant [x1, y1, x2, y2], 
                 les coordonnées des coins opposés du rectangle.

    retour :
        Tuple (x, y) représentant le centre du rectangle.

    >>> get_center([0, 0, 10, 10])
    (5.0, 5.0)
    >>> get_center([2, 4, 6, 8])
    (4.0, 6.0)
    >>> get_center([-10, -10, 10, 10])
    (0.0, 0.0)
    >>> get_center((0, 0, 0, 0))
    (0.0, 0.0)
    >>> get_center([1.5, 2.5, 3.5, 4.5])
    (2.5, 3.5)

    """
    return ( (coords[0] + coords[2]) / 2, (coords[1] + coords[3]) / 2 )

def find_click_point(click_point, sommets, min_dist):
    """
    Trouve l'index du sommet le plus proche d'un point cliqué, si la distance est inférieure à un seuil.

    Paramètres :
        click_point : tuple (x, y), coordonnées du clic.
        sommets : liste de tuples (x, y).
        min_dist : distance seuil.

    Retour :
        Index du sommet le plus proche, ou None.
    """
    closest_idx = None
    closest_dist = min_dist

    for i in range(len(sommets)):
        x, y = sommets[i]
        dist = math.dist(click_point, (x, y))
        if dist < closest_dist:
            closest_idx = i
            closest_dist = dist

    return closest_idx

def calculate_angle(p1, p2):
    """
    Calcule l'angle (en radians) entre deux points p1 et p2, dans [0, 2π).
    """
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    return math.atan2(dy, dx) % (2 * math.pi)