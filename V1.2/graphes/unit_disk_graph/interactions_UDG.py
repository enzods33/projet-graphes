import math
import interface_graphique.interactions_canvas as ic
import outils_canva.geometrie as geo
from outils_canva.constantes import RAYON_PAR_DEFAUT

# Variables globales
lbl_rayon = None
rayon_affiche = RAYON_PAR_DEFAUT  # Ce que l'utilisateur voit
facteur_global = 1.0  # Facteur d'échelle cumulé

def left_click(event):
    """
    Gère le clic gauche sur le canvas : ajoute un point et crée les arêtes correspondantes.
    """
    point = ic.create_point(event.x, event.y)
    ic.sommets.append(point)
    create_edges(point)

def create_edges(new_point):
    """
    Crée des arêtes entre un nouveau point et ses voisins existants si connectés.
    """
    for sommet in ic.sommets:
        if sommet != new_point and is_connected(new_point, sommet):
            center1 = geo.get_center(ic.canva.coords(new_point))
            center2 = geo.get_center(ic.canva.coords(sommet))
            ic.canva.create_line(center1[0], center1[1], center2[0], center2[1], fill="yellow", width=2)
    ic.update_compteur()

def reafficher_les_aretes():
    """
    Recalcule et réaffiche toutes les arêtes du graphe correctement.
    """
    for item in ic.canva.find_all():
        if ic.canva.type(item) == "line":
            ic.canva.delete(item)

    sommets = ic.sommets
    for i in range(len(sommets)):
        for j in range(i + 1, len(sommets)):
            if is_connected(sommets[i], sommets[j]):
                center1 = geo.get_center(ic.canva.coords(sommets[i]))
                center2 = geo.get_center(ic.canva.coords(sommets[j]))
                ic.canva.create_line(center1[0], center1[1], center2[0], center2[1], fill="yellow", width=2)
    ic.update_compteur()

def augmenter_rayon(event=None):
    global rayon_affiche
    rayon_affiche += 10
    maj_label()
    reafficher_les_aretes()

def diminuer_rayon(event=None):
    global rayon_affiche
    if rayon_affiche > 10:
        rayon_affiche -= 10
        maj_label()
        reafficher_les_aretes()

def set_lbl_rayon(label):
    global lbl_rayon
    lbl_rayon = label

def maj_label():
    if lbl_rayon:
        lbl_rayon.config(text=f"Rayon : {round(rayon_affiche)}")

def reset_specifique():
    global rayon_affiche, facteur_global
    rayon_affiche = RAYON_PAR_DEFAUT
    facteur_global = 1.0
    maj_label()

def get_rayon():
    return rayon_affiche

def is_connected(point1, point2):
    center1 = geo.get_center(ic.canva.coords(point1))
    center2 = geo.get_center(ic.canva.coords(point2))
    distance_canvas = math.dist(center1, center2)
    distance_reelle = distance_canvas / facteur_global
    return distance_reelle <= rayon_affiche

def get_parametres():
    return {"rayon": rayon_affiche}

def set_parametres(parametres):
    global rayon_affiche
    rayon_affiche = parametres.get("rayon", RAYON_PAR_DEFAUT)
    maj_label()

def get_type_graphe():
    return "Unit disk graph"

def set_facteur_global(factor):
    global facteur_global
    facteur_global *= factor
