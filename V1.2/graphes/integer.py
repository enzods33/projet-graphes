# L'interface graphique

from interface_graphique.interface_graphe import build_graph_interface
import math
from interface_graphique import interactions_canvas as ic

def open_integer_graph(root):
    """
    Crée l'interface du graphe entier et enregistre ses callbacks propres.
    """
    build_graph_interface(
        root,
        {
            'is_connected': is_connected,
            'get_graph_type': get_graph_type,
        },
        ajouter_boutons_specifiques=None,
        graph_name=get_graph_type()
    )

# Fonctions d'intégration du graphe

def get_graph_type():
    """
    Retourne le nom du graphe utilisé pour l'affichage et la sauvegarde.
    """
    return "Integer graph"

# Algorithme principal du graphe Integer Graph

def is_connected(idx1, idx2):
    """
    Détermine si deux sommets doivent être connectés si la distance entre eux est presque entière.

    Retourne :
        True si la distance est à moins de 1e-3 d'un entier, False sinon.
    """
    p1 = ic.sommets.points[idx1]
    p2 = ic.sommets.points[idx2]
    distance = math.dist(p1, p2)
    return abs(distance - round(distance)) <= 1e-3