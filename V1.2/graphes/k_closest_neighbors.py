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

# Cache global pour ne pas recalculer à chaque appel
k_neighbors_cache = {}
last_points_hash = None

def is_connected(idx1, idx2):
    """
    Deux sommets sont connectés si l'un est dans les k plus proches voisins de l'autre (symétrique).
    """
    global last_points_hash, k_neighbors_cache

    points = ic.sommets.points
    current_hash = (hash(tuple(points)), k_voisins)

    if current_hash != last_points_hash:
        last_points_hash = current_hash
        k_neighbors_cache = compute_all_neighbors(points, k_voisins)

    return idx2 in k_neighbors_cache[idx1] or idx1 in k_neighbors_cache[idx2]

def compute_all_neighbors(points, k):
    """
    Pré-calcule les k plus proches voisins pour chaque point une seule fois.
    """
    neighbors = {}
    for i in range(len(points)):
        distances = []
        for j in range(len(points)):
            if i != j:
                dist = ic.get_real_distance(i, j)
                distances.append((j, dist))
        distances.sort(key=lambda x: x[1])
        neighbors[i] = [idx for idx, _ in distances[:k]]
    return neighbors