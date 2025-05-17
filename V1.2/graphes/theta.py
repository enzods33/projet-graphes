#L'interface graphique

from interface_graphique.interface_graphe import build_graph_interface
from interface_graphique.ui.boutons_graphes import add_plus_minus_buttons
from interface_graphique import interactions_canvas as ic
from interface_graphique.interactions_canvas.cache_distance import get_real_distance
import math

def open_theta_graph(root):
    build_graph_interface(
        root,
        {
            'is_connected': is_connected,
            'get_graph_type': get_graph_type,
            'get_parameters': get_parameters,
            'set_parameters': set_parameters,
            'reset': reset_theta_graph
        },
        ajouter_boutons_specifiques=lambda frame: add_plus_minus_buttons(
            frame,
            lambda: adjust_k(1),
            lambda: adjust_k(-1),
            get_k_label_text,
            set_k_label_widget
        ),
        graph_name=get_graph_type()
    )

#Fonctions d'intégration du graphe

theta_k = 2
label_k = None

def get_graph_type():
    return "Theta graph"

def get_parameters():
    return {"k": theta_k}

def set_parameters(params):
    global theta_k
    theta_k = params.get("k", 8)

def reset_theta_graph():
    global theta_k
    theta_k = 2
    update_k_label()

#Contrôle de k et affichage du label

def adjust_k(delta):
    global theta_k
    if theta_k + delta >= 1:
        theta_k += delta
        update_k_label()
        ic.redraw_canvas()

def get_k_label_text():
    return f"k : {theta_k}"

def update_k_label():
    if label_k and label_k.winfo_exists():
        label_k.config(text=get_k_label_text())

def set_k_label_widget(lbl):
    global label_k
    label_k = lbl
    update_k_label()

#Algorithme principal du graphe Theta

last_theta_hash = None


def is_connected(i, j):
    points=ic.sommets.points
    cone_neighbors_i = get_theta_neighbors(i, points, theta_k)
    cone_neighbors_j = get_theta_neighbors(j, points, theta_k)
    return j in cone_neighbors_i or i in cone_neighbors_j


def get_theta_neighbors(p_idx, points, k):
    """
    Retourne les indices des voisins de p_idx sélectionnés selon l'algorithme Theta.
    Ne recalcule que si les points ou k ont changé.
    """
    global theta_neighbors_cache, last_theta_hash

    # On calcule un nombre entier unique (ou presque) qui représente le "l'identité" de l’objet (liste = pas hashable, mais tuple oui).
    # Pour éviter de recalculer les voisins Theta si la position n'a pas changé
    current_hash = (hash(tuple(points)), k)  

    # Si les points ou k ont changé, on vide complètement le cache
    if current_hash != last_theta_hash:
        last_theta_hash = current_hash
        theta_neighbors_cache = {}

    if p_idx in theta_neighbors_cache:
        return theta_neighbors_cache[p_idx]
    
    origin = points[p_idx]
    cone_width = 2 * math.pi / k
    cones = [None] * k

    for i in range(len(points)):
        if i == p_idx:
            continue
        v = points[i]
        angle = math.atan2(v[1] - origin[1], v[0] - origin[0]) % (2 * math.pi)
        cone_idx = int(angle / cone_width)
        dist = get_real_distance(p_idx, i)

        if cones[cone_idx] is None or dist < cones[cone_idx][1]:
            cones[cone_idx] = (i, dist)

    voisins = [item[0] for item in cones if item is not None]
    theta_neighbors_cache[p_idx] = voisins
    return voisins