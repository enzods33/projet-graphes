from interface_graphique import interactions_canvas as ic

mst_edges = []

def get_all_edges(sommets):
    edges = []
    for i in range(len(sommets)):
        for j in range(i + 1, len(sommets)):    #i+1 pour ne pas avoir 2 fois le meme
            dist = ic.get_real_distance(i, j)
            edges.append((dist, i, j))
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
        liste : dictionnaire qui associe chaque élément à son parent dans la structure.
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



def is_connected(idx1, idx2):
    """
    Vérifie si deux sommets sont connectés dans le graphe minimum_spanning_tree

    Paramètres :
        idx1 : indice du premier sommet
        idx2 : indice du deuxième sommet

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
    parent = {i: i for i in range(len(sommets))}                #Un dictionnaire parent est créé pour chaque sommet.
    #Initialement, chaque sommet est son propre parent, ce qui signifie que chaque sommet forme un ensemble disjoint.   


    mst_edges = []
    for dist, u, v in edges:
        if find(u, parent) != find(v, parent):
            union(u, v, parent)
            mst_edges.append((u, v))

    return (idx1, idx2) in mst_edges or (idx2, idx1) in mst_edges

def get_graph_type():
    """
    Retourne le type du graphe actuellement utilisé ("Minimum spanning tree graph").
    """
    return "Minimum spanning tree graph"