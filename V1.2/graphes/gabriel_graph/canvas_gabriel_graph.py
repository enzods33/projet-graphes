from interface_graphique.creer_graph import creer_graph
from graphes.gabriel_graph import interactions_gabriel_graph as i_gg

def ouvrir_canvas_gabriel_graph(root):
    creer_graph(root, {
        'is_connected': i_gg.is_connected,
        'get_type_graphe': i_gg.get_type_graphe,
    })
