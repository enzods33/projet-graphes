from interface_graphique.creer_graph import create_graph
from graphes.k_closest_neighbors_graph import interactions_k_closest_neighbors_graph as i_kcng
from interface_graphique.ui.boutons import add_kcng_buttons

def open_k_closest_neighbors_graph_canvas(root):
    create_graph(
        root,
        {
            'is_connected': i_kcng.is_connected,
            'get_type_graphe': i_kcng.get_type_graphe,
            'get_parametres': i_kcng.get_parametres,
            'set_parametres': i_kcng.set_parametres,
            'reset': i_kcng.reset_specifique,
        },
        ajouter_boutons_specifiques=lambda frame: add_kcng_buttons(
            frame,
            augmenter_cb=lambda: i_kcng.ajuster_k(1),
            diminuer_cb=lambda: i_kcng.ajuster_k(-1),
            get_lbl_text=lambda: f"k = {i_kcng.get_k()}",
            set_lbl_k_cb=i_kcng.set_lbl_k
        ),
        graph_name = i_kcng.get_type_graphe()
    )