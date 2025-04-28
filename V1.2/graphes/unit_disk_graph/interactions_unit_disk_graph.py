import math

import interface_graphique.interactions_canvas as ic
import outils_canva.geometrie as geo
from outils_canva.constantes import RAYON_PAR_DEFAUT, COULEUR_ARETE, LARGEUR_ARETE

# Variables globales
lbl_rayon = None
rayon_affiche = RAYON_PAR_DEFAUT    # Ce que l'utilisateur voit
facteur_global = 1.0                # Facteur d'échelle cumulé

def is_connected(point1, point2):
    """
    Détermine si deux sommets doivent être connectés selon la distance réelle (après zoom éventuel).

    Retourne :
        True si les deux sommets sont connectés (distance <= rayon affiché), False sinon.
    """
    center1 = geo.get_center(ic.canva.coords(point1))
    center2 = geo.get_center(ic.canva.coords(point2))
    distance_canvas = math.dist(center1, center2)
    distance_reelle = distance_canvas / facteur_global
    return distance_reelle <= rayon_affiche

def create_edges(new_point):
    """
    Crée des arêtes entre un nouveau sommet et tous les sommets existants qui sont connectés.
    """
    for sommet in ic.sommets:
        if sommet != new_point and is_connected(new_point, sommet):
            center1 = geo.get_center(ic.canva.coords(new_point))
            center2 = geo.get_center(ic.canva.coords(sommet))
            ic.canva.create_line(center1[0], center1[1], center2[0], center2[1], fill=COULEUR_ARETE, width=LARGEUR_ARETE)
    ic.update_compteur()

def left_click(event):
    """
    Gère le clic gauche : ajoute un sommet au canvas et connecte automatiquement ce sommet aux autres.
    """
    point = ic.create_point(event.x, event.y)
    ic.sommets.append(point)
    create_edges(point)

def reafficher_les_aretes():
    """
    Recalcule et réaffiche toutes les arêtes du graphe en fonction des sommets présents.
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

def ajuster_rayon(delta: int, event=None):
    """
    Ajuste dynamiquement le rayon affiché (augmenter ou diminuer).

    Paramètres :
        delta : nombre à ajouter au rayon (positif ou négatif).
        event : (optionnel) événement Tkinter associé.
    """
    global rayon_affiche
    if delta > 0 or (delta < 0 and rayon_affiche + delta >= 10):
        rayon_affiche += delta
        maj_label()
        reafficher_les_aretes()

def reset_specifique():
    """
    Réinitialise le rayon et le facteur de zoom global aux valeurs par défaut.
    """
    global rayon_affiche, facteur_global
    rayon_affiche = RAYON_PAR_DEFAUT
    facteur_global = 1.0
    maj_label()

def set_lbl_rayon(label):
    """
    Associe un widget Label pour afficher dynamiquement la valeur du rayon.
    """
    global lbl_rayon
    lbl_rayon = label

def maj_label():
    """
    Met à jour le texte du label associé pour afficher la valeur actuelle du rayon.
    """
    if lbl_rayon:
        lbl_rayon.config(text=f"Rayon : {round(rayon_affiche)}")

def get_rayon():
    """
    Retourne la valeur actuelle du rayon affiché.
    """
    return rayon_affiche

def get_parametres():
    """
    Retourne les paramètres actuels du graphe sous forme de dictionnaire.
    """
    return {"rayon": rayon_affiche}

def set_parametres(parametres):
    """
    Applique les paramètres du graphe fournis sous forme de dictionnaire (met à jour le rayon).
    """
    global rayon_affiche
    rayon_affiche = parametres.get("rayon", RAYON_PAR_DEFAUT)
    maj_label()

def get_type_graphe():
    """
    Retourne le type du graphe actuellement utilisé ("Unit disk graph").
    """
    return "Unit disk graph"

def set_facteur_global(factor):
    """
    Met à jour le facteur global d'échelle (utilisé après un zoom sur le canvas).
    """
    global facteur_global
    facteur_global *= factor