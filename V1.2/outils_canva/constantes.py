"""
Module qui regroupe toutes les variables utiles et modifiables par l'utilisateur
afin d'influer sur l'utilisation des graphes et du canva
"""

# Canvas
CANVAS_LARGEUR = 600
CANVAS_HAUTEUR = 600
CANVAS_COULEUR = "white"

# Root
ROOT_LARGEUR = 800
ROOT_HAUTEUR = 600

# Scrollbar
SCROLLX1 = -CANVAS_LARGEUR*5
SCROLLY1 = -CANVAS_HAUTEUR*5
SCROLLX2 = CANVAS_LARGEUR*5
SCROLLY2 = CANVAS_HAUTEUR*5

# Points
TAILLE_POINT = 3
COULEUR_POINT = "yellow"
MAX_NB_POINTS = 75

# Arêtes
COULEUR_ARETE = "yellow"
LARGEUR_ARETE = 2

# Zoom
ZOOM_IN_FACTOR = 1.1
ZOOM_OUT_FACTOR = 0.9

# Paramètres géométrie
MIN_DIST = 5 

# Limites de zoom
ZOOM_MIN = 0.1
ZOOM_MAX = 10.0  

# Spécifiques UDG 
RAYON_PAR_DEFAUT_Udg = 100
RAYON_MODIFICATION_Udg = 10 
RAYON_MAX_Udg = 8500

# Spécifique Yao graph
K_INITIAL_Yao = 2
K_MAX_Yao = 18

# Spécifique k closest neighbors
K_INITIAL_Neighbors = 3
K_MAX_Neighbors = 30