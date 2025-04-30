import math
import tkinter as tk

import interface_graphique.interactions_canvas as ic
import outils_canva.geometrie as geo
from outils_canva.constantes import RAYON_PAR_DEFAUT, COULEUR_ARETE, LARGEUR_ARETE

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
        ic.update_edge()

def reset_specifique():
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
        try:
            lbl_rayon.config(text=f"Rayon : {round(rayon_affiche)}")
        except tk.TclError:
            lbl_rayon = None
            
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