from interface_graphique.creer_graph import create_graph
from graphes.yao_graph import interactions_yao_graph as i_yg
from interface_graphique.ui.boutons import add_plus_minus_buttons

def open_yao_graph_canvas(root):
    """Crée le canvas pour le graphe de Yao."""

    create_graph(
        root,
        {
            'is_connected': i_yg.is_connected,
            'get_graph_type': i_yg.get_graph_type,
            'get_parameters': i_yg.get_parameters,
            'set_parameters': i_yg.set_parameters,
            'reset': i_yg.reset_specific  
        },
        graph_name=i_yg.get_graph_type()
    )