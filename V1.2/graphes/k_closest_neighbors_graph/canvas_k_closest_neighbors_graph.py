from interface_graphique.creer_graph import create_graph
from graphes.k_closest_neighbors_graph import interactions_k_closest_neighbors_graph as i_kcng
from interface_graphique.ui.boutons import add_kcng_buttons

def open_k_closest_neighbors_graph_canvas(root):
    """créé le graphe en enregistrant les carcateristiques propres a ce graphe"""

    create_graph(
        root,
        {
            'is_connected': i_kcng.is_connected,
            'get_graph_type': i_kcng.get_graph_type,
            'get_parameters': i_kcng.get_parameters,
            'set_parameters': i_kcng.set_parameters,
            'reset': i_kcng.specific_reset,
        },
        ajouter_boutons_specifiques=lambda frame: add_kcng_buttons(
            frame,
            augmenter_cb=lambda: i_kcng.adjust_k(1),
            diminuer_cb=lambda: i_kcng.adjust_k(-1),
            get_lbl_text=lambda: f"k = {i_kcng.get_k()}",
            set_lbl_k_cb=i_kcng.set_lbl_k
        ),
        graph_name = i_kcng.get_graph_type()
    )