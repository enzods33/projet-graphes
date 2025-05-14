import tkinter as tk

import interface_graphique.interactions_canvas as ic
from outils_canva.constantes import RAYON_PAR_DEFAUT

# Variables globales
lbl_rayon = None
rayon_affiche = RAYON_PAR_DEFAUT    # Ce que l'utilisateur voit 

def is_connected(point1, point2):
    """
    Détermine si deux sommets doivent être connectés selon la distance réelle (après zoom éventuel).

    Retourne :
        True si les deux sommets sont connectés (distance <= rayon affiché), False sinon.
    """
    return ic.get_real_distance(point1, point2) <= rayon_affiche

def adjust_radius(delta: int, event=None):
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
        ic.update_edge()

def specific_reset():
    """
    Réinitialise le rayon et le facteur de zoom global aux valeurs par défaut.
    """
    global rayon_affiche
    rayon_affiche = RAYON_PAR_DEFAUT
    maj_label()

def set_lbl_rayon(label):
    """
    Associe un widget Label pour afficher dynamiquement la valeur du rayon.
    """
    global lbl_rayon
    lbl_rayon = label

def maj_label():
    global lbl_rayon
    if lbl_rayon:
        lbl_rayon.config(text=f"Rayon : {round(rayon_affiche)}")

def get_radius():
    """
    Retourne la valeur actuelle du rayon affiché.
    """
    return f"Rayon : {rayon_affiche}"

def get_parameters():
    """
    Retourne les paramètres actuels du graphe sous forme de dictionnaire.
    """
    return {"rayon": rayon_affiche}

def set_parameters(parametres):
    """
    Applique les paramètres du graphe fournis sous forme de dictionnaire (met à jour le rayon).
    """
    global rayon_affiche
    rayon_affiche = parametres.get("rayon", RAYON_PAR_DEFAUT)
    maj_label()

def get_graph_type():
    """
    Retourne le type du graphe actuellement utilisé ("Unit disk graph").
    """
    return "Unit disk graph"