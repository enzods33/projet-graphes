"""
Module qui regroupe toutes les variables utiles et modifiables par l'utilisateur
afin d'influer sur l'utilisation des graphes et du canva
"""


# Root
ROOT_LARGEUR = 800
ROOT_HAUTEUR = 600

# Canvas
CANVAS_LARGEUR = 600
CANVAS_HAUTEUR = 600
CANVAS_COULEUR = "white"

SCROLLX1 = -CANVAS_LARGEUR*5
SCROLLY1 = -CANVAS_HAUTEUR*5
SCROLLX2 = CANVAS_LARGEUR*5
SCROLLY2 = CANVAS_HAUTEUR*5

# Points
TAILLE_POINT = 3
COULEUR_POINT = "yellow"

# Arêtes
COULEUR_ARETE = "yellow"
LARGEUR_ARETE = 2

# Zoom
ZOOM_IN_FACTOR = 1.1
ZOOM_OUT_FACTOR = 0.9

# Déplacement
MOVE_STEP = 20

# Spécifiques UDG 
RAYON_PAR_DEFAUT = 100
RAYON_MODIFICATION = 10 

# Paramètres géométrie
MIN_DIST = 5  # Distance minimale pour considérer qu'un point est proche

# Nuage aléatoire
MAX_NB_POINTS = 100 

# Limites de zoom
ZOOM_MIN = 0.11
ZOOM_MAX = 10.0  