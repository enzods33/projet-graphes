from interface_graphique.creer_graph import create_graph
from graphes.yao_graph import interactions_yao_graph as i_yg
from interface_graphique.ui.boutons import add_yao_buttons

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
        ajouter_boutons_specifiques=lambda frame: add_yao_buttons(frame, i_yg.augmenter_k, i_yg.diminuer_k, i_yg.get_label_k_text, i_yg.set_label_k),
        graph_name=i_yg.get_graph_type()
    )