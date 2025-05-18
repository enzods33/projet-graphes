#L'interface graphique

from interface_graphique.interface_graphe import build_graph_interface
from interface_graphique.ui.boutons_graphes import add_plus_minus_buttons
import interface_graphique.interactions_canvas as ic
from outils_canva.constantes import K_INITIAL_Neighbors, K_MAX_Neighbors

def open_k_closest_neighbors_graph(root):
    build_graph_interface(
        root,
        {
            'is_connected': is_connected,
            'get_graph_type': get_graph_type,
            'get_parameters': get_parameters,
            'set_parameters': set_parameters,
            'reset': reset_k_closest_neighbors_graph,
        },
        ajouter_boutons_specifiques=lambda frame_buttons: add_plus_minus_buttons(
            frame_buttons,
            lambda: adjust_k(1),
            lambda: adjust_k(-1),
            get_k_label_text,
            set_k_label_widget
        ),
        graph_name=get_graph_type()
    )

#Fonctions d'intégration du graphe


k_voisins = K_INITIAL_Neighbors  # Valeur par défaut
lbl_k = None
def get_graph_type():
    return "K closest neighbors graph"

def get_parameters():
    return {"k": k_voisins}

def set_parameters(parametres):
    global k_voisins
    k_voisins = parametres.get("k", 3)
    update_k_label()

def reset_k_closest_neighbors_graph():
    global k_voisins
    k_voisins = K_INITIAL_Neighbors
    update_k_label()

#Contrôle de k et affichage du label

def adjust_k(delta):
    global k_voisins
    nouveau_k = k_voisins + delta
    if 1 <= nouveau_k <= K_MAX_Neighbors:
        k_voisins = nouveau_k
        update_k_label()
        ic.redraw_canvas()

def get_k_label_text():
    return f"k = {k_voisins}"

def update_k_label():
    if lbl_k and lbl_k.winfo_exists():
        lbl_k.config(text=get_k_label_text())

def set_k_label_widget(label):
    global lbl_k
    lbl_k = label
    update_k_label()

#Algorithme principal du graphe K Closest Neighbors

def is_connected(idx1, idx2):
    """
    Deux sommets sont connectés si l'un est dans les k plus proches voisins de l'autre (symétrique).
    """
    # On force le remplissage du cache pour cette paire
    ic.get_real_distance(idx1, idx2)
    voisins1 = find_neighbors(idx1, k_voisins)
    if idx2 in voisins1:
        return True

    voisins2 = find_neighbors(idx2, k_voisins)
    return idx1 in voisins2

def find_neighbors(idx_point, k):
    """
    Retourne les k plus proches voisins de idx_point
    à partir des distances déjà présentes dans le cache.
    """
    voisins = []
    for (i, j), dist in ic.cache_distance.distance_cache.items():
        if i == idx_point:
            voisins.append((j, dist))
        elif j == idx_point:
            voisins.append((i, dist))

    voisins.sort(key=lambda x: x[1])
    return [idx for idx, _ in voisins[:k]]