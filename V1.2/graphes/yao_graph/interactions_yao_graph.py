"""A CORRIGER, YA DES ERRURES"""
import math
from interface_graphique import interactions_canvas as ic

nb_secteurs = 3
label_k = None

def set_parameters(parametres):
    """Permet d'ajuster dynamiquement le nombre de secteurs"""
    global nb_secteurs
    if 'nb_secteurs' in parametres:
        nb_secteurs = parametres['nb_secteurs']

def get_parameters():
    """Retourne les paramètres actuels (nombre de secteurs)"""
    return {'nb_secteurs': nb_secteurs}

def get_graph_type():
    """Type du graphe pour la sauvegarde/chargement."""
    return "Yao Graph"

def reset_specific():
    """Remet le Yao Graph à l'état initial : k = 6."""
    global nb_secteurs
    nb_secteurs = 3
    if label_k:
        label_k.config(text=get_label_k_text())

def augmenter_k():
    global label_k
    params = get_parameters()
    params['nb_secteurs'] += 1
    set_parameters(params)
    if label_k:
        label_k.config(text=get_label_k_text())
    from interface_graphique import interactions_canvas as ic
    ic.redraw_canvas()

def diminuer_k():
    global label_k
    params = get_parameters()
    if params['nb_secteurs'] > 1:
        params['nb_secteurs'] -= 1
        set_parameters(params)
        if label_k:
            label_k.config(text=get_label_k_text())
        from interface_graphique import interactions_canvas as ic
        ic.redraw_canvas()

def get_label_k_text():
    return f"k = {get_parameters()['nb_secteurs']}"

def set_label_k(lbl):
    global label_k
    label_k = lbl


def is_connected(idx1, idx2):
    """
    Détermine si une arête orientée part du sommet idx1 vers idx2 dans le Yao Graph.
    
    Chaque sommet divise l'espace autour de lui en nb_secteurs secteurs,
    et connecte vers le plus proche sommet dans chaque secteur.
    """
    sommets = ic.sommets
    p1 = sommets[idx1]
    p2 = sommets[idx2]

    voisins = trouver_voisins(idx1)

    return idx2 in voisins

def trouver_voisins(idx_source):
    """
    Pour un sommet donné (idx_source), retourne la liste des indices de ses voisins directs
    (plus proche sommet dans chaque secteur).
    """
    sommets = ic.sommets
    x0, y0 = sommets[idx_source]
    
    candidats = [[] for _ in range(nb_secteurs)]

    for idx, (x, y) in enumerate(sommets):
        if idx == idx_source:
            continue

        dx = x - x0
        dy = y - y0
        angle = math.atan2(dy, dx)  # Angle du point (x,y) au point (x0,y0)
        if angle < 0:
            angle += 2 * math.pi

        secteur = int(nb_secteurs * angle / (2 * math.pi))

        distance = math.dist((x0, y0), (x, y))
        candidats[secteur].append((distance, idx))

    voisins = []
    for liste in candidats:
        if liste:
            liste.sort()
            voisins.append(liste[0][1])  # On garde le plus proche dans le secteur
    
    return voisins