# Interactions pour le graphe minimum_spanning_tree_graph

from interface_graphique import interactions_canvas as ic

mst_edges = []

def get_all_edges(liste):
    """
    construit une liste de toutes les aretes possible, avec leurs longueurs
    paramètres :
        sommets (list) : Liste des sommets du graphe.

    retour :
        list : Liste de tuples (distance, sommet1, sommet2), représentant les arêtes
    """
    edges = []
    for i in range(len(liste)):
        for j in range(i + 1, len(liste)):        #i+1 pour ne pas avoir deux fois le même
            u, v = liste[i], liste[j]
            dist = ic.get_real_distance(u, v)
            edges.append((dist, u, v))
    return edges


"""
à présent, utilisation du 'union-find'
    Lorsqu'on gère des ensembles de valeurs groupées (par exemple dans l'algorithme du MST), 
    on utilise une structure appelée "Union-Find" pour savoir si deux éléments appartiennent au même groupe.
    Chaque élément pointe vers un "parent", et le parent d'un parent, etc., jusqu'à une racine 
    (lui-même son propre parent), qui représente l'ensemble
"""


def find(s, liste):
    """
    Trouve le représentant de l'ensemble auquel appartient le sommet s 
    (avec compression de chemin, c'est a dire afin de raccourcir le chemin pour les futurs appels pour accélérer les recherches)

    Paramètres :
        parent : dictionnaire qui associe chaque élément à son parent dans la structure.
                        si un élément est son propre parent, c'est la racine
        s : l'élément dont on veut connaître la racine.

    renvoie la racine de l'ensemble contenant s
    """
    while liste[s] != s:
            liste[s] = liste[liste[s]]
            s = liste[s]
    return s

def union(a, b, liste):
    """
    Fusionne les ensembles contenant les sommets a et b.
    paramètres :
        parent : dictionnaire des parents
        a : un sommet
        b : un autre sommet
    """
    liste[find(a,liste)] = find(b,liste)



def is_connected(p1, p2):
    """
    Vérifie si deux sommets sont connectés dans le graphe minimum_spanning_tree

    Paramètres :
        p1 : premier sommet
        p2 : deuxième sommet

    Retour :
        bool : True si les deux sommets sont connectés dans le MST, False sinon.
    """
     
    global mst_edges

    sommets = ic.sommets
    if len(sommets) < 2:
        mst_edges = []
        return False

    edges = get_all_edges(sommets)
    edges.sort()                       #on trie les arêtes par distance croissante
    parent = {s: s for s in sommets}                #Un dictionnaire parent est créé pour chaque sommet.
    #Initialement, chaque sommet est son propre parent, ce qui signifie que chaque sommet forme un ensemble disjoint.   


    mst_edges = []
    for dist, u, v in edges:
        if find(u, parent) != find(v, parent):
            union(u, v, parent)
            mst_edges.append((u, v))

    return (p1, p2) in mst_edges or (p2, p1) in mst_edges

def get_type_graphe():
    """
    Retourne le type du graphe actuellement utilisé ("Minimum spanning tree graph").
    """
    return "Minimum spanning tree graph"