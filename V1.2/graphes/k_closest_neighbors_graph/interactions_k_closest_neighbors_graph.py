import tkinter as tk
import interface_graphique.interactions_canvas as ic

# Variables globales
lbl_k = None
k_voisins = 3  # valeur par défaut de k


def get_k():
    """
    Retourne le nombre de k voisin actuellement.
    """
    return f"k = {k_voisins}"


def find_neighbors(idx_point, points, k):
    """
    Trouve les k plus proches voisins du point donné parmi les sommets.
    """
    dists = [
        (idx, ic.get_real_distance(idx_point, idx))
        for idx in range(len(points)) if idx != idx_point
    ]
    dists.sort(key=lambda x: x[1])
    return [idx for idx, _ in dists[:k]]


def is_connected(p1, p2):
    """
    Détermine si p1 et p2 doivent être connectés dans un k-NN graph symétrique.
    """
    voisins1 = find_neighbors(p1, ic.sommets, k_voisins)
    if p2 in voisins1:
        return True

    voisins2 = find_neighbors(p2, ic.sommets, k_voisins)
    return p1 in voisins2


def adjust_k(delta):
    """
    Augmente ou diminue la valeur de k.
    """
    global k_voisins
    if k_voisins + delta >= 1:
        k_voisins += delta
        maj_label()
        ic.update_edge()


def specific_reset():
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
        lbl_k.config(text=f"k = {k_voisins}")


def get_parameters():
    return {"k": k_voisins}

def set_parameters(parametres):
    global k_voisins
    k_voisins = parametres.get("k", 3)
    maj_label()

def get_graph_type():
    return "K closest neighbors graph"