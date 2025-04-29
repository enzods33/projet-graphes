import tkinter as tk
import interface_graphique.interactions_canvas as ic

# Variables globales
lbl_k = None
k_voisins = 3  # valeur par défaut de k


def get_k():
    return k_voisins


def trouver_voisins(point, sommets, k):
    """
    Trouve les k plus proches voisins du point donné parmi les sommets.
    """
    dists = [
        (p, ic.get_distance_reelle(point, p))
        for p in sommets if p != point
    ]
    dists_triees = sorted(dists, key=lambda x: x[1])
    voisins = [p for p, _ in dists_triees[:k]]
    return voisins


def is_connected(p1, p2):
    """
    Détermine si p1 et p2 doivent être connectés dans un k-NN graph symétrique.
    """
    voisins1 = trouver_voisins(p1, ic.sommets, k_voisins)
    if p2 in voisins1:
        return True

    voisins2 = trouver_voisins(p2, ic.sommets, k_voisins)
    return p1 in voisins2


def ajuster_k(delta):
    """
    Augmente ou diminue la valeur de k.
    """
    global k_voisins
    if k_voisins + delta >= 1:
        k_voisins += delta
        maj_label()
        ic.reafficher_les_aretes()


def reset_specifique():
    """
    Réinitialise la valeur de k à 3.
    """
    global k_voisins
    k_voisins = 3
    maj_label()

def set_lbl_k(label):
    global lbl_k
    lbl_k = label

def maj_label():
    global lbl_k
    if lbl_k:
        try:
            lbl_k.config(text=f"k = {k_voisins}")
        except tk.TclError:
            lbl_k = None

def get_parametres():
    return {"k": k_voisins}

def set_parametres(parametres):
    global k_voisins
    k_voisins = parametres.get("k", 3)
    maj_label()

def get_type_graphe():
    return "K closest neighbors graph"