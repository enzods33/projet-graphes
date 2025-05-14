import math
from interface_graphique import interactions_canvas as ic

theta_edges = []
theta_k = 2
label_k = None
last_n_points = 0
last_positions = []  


def reset_specific():
    """Remet le Theta Graph à son état initial."""

    global theta_edges, theta_k, label_k, last_n_points, last_positions

    theta_edges = []
    theta_k = 2
    last_n_points = 0
    last_positions = []

    if label_k:
        label_k.config(text=get_lbl_text())

def get_graph_type():
    """
    Retourne le type du graphe actuellement utilisé ("Theta graph").
    """
    return "Theta graph"

def get_parameters():
    """
    Retourne les paramètres actuels du Theta Graph sous forme de dictionnaire.
    """
    return {"k": theta_k}

def set_parameters(parametres):
    """
    Applique les paramètres donnés pour le Theta Graph (met à jour k si fourni).
    """
    global theta_k
    theta_k = parametres.get("k", 8)  # Si k n'est pas donné, on remet 8
    rebuild_theta_edges()  # On reconstruit directement

def augmenter_k():
    """
    Augmente le nombre de cônes du Theta Graph et met à jour l'affichage.
    """
    global theta_k
    theta_k += 1
    if theta_k > 50:
        theta_k = 50
    rebuild_theta_edges()
    ic.update_edge()
    maj_label()

def diminuer_k():
    """
    Diminue le nombre de cônes du Theta Graph et met à jour l'affichage.
    """
    global theta_k
    theta_k -= 1
    if theta_k < 1:
        theta_k = 1
    rebuild_theta_edges()
    ic.update_edge()
    maj_label()

def get_lbl_text():
    """
    Retourne le texte actuel du label affichant k.
    """
    return f"k : {theta_k}"

def maj_label():
    """
    Met à jour l'affichage du label de k si le label existe.
    """
    if label_k and label_k.winfo_exists():
        label_k.config(text=get_lbl_text())

def set_lbl_k(lbl):
    """
    Enregistre le label Tkinter pour afficher le nombre de cônes.
    """
    global label_k
    label_k = lbl
    maj_label()

def calculate_angle(p1, p2):
    """
    Calcule l'angle entre deux points p1 et p2 en radians.
    """
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    return math.atan2(dy, dx) % (2 * math.pi)

def project_point_on_ray(origin, angle, point):
    """
    Projette orthogonalement 'point' sur la droite passant par 'origin' avec l'angle donné.
    
    Retourne la distance projetée le long de la direction.
    """
    dx = point[0] - origin[0]
    dy = point[1] - origin[1]
    return dx * math.cos(angle) + dy * math.sin(angle)

def select_closest_in_cone(p_idx, sommets, k):
    """
    Pour un sommet donné, sélectionne le meilleur voisin dans chaque cône.
    """
    p = sommets[p_idx]
    cone_width = 2 * math.pi / k
    cones = [None] * k

    for v_idx, v in enumerate(sommets):
        if v_idx == p_idx:
            continue

        angle = calculate_angle(p, v)
        cone_idx = int(angle / cone_width)

        proj = project_point_on_ray(p, cone_idx * cone_width + cone_width/2, v)

        if cones[cone_idx] is None or proj < cones[cone_idx][0]:
            cones[cone_idx] = (proj, v_idx)

    edges = []
    for item in cones:
        if item is not None:
            _, voisin_idx = item
            edges.append((p_idx, voisin_idx))

    return edges

def rebuild_theta_edges():
    """
    Reconstruit toutes les arêtes du Theta Graph.
    """
    global theta_edges
    global last_n_points
    global last_positions

    sommets = ic.sommets
    last_n_points = len(sommets)
    last_positions = list(sommets)  # Copie profonde des positions

    all_edges = set()

    for p_idx in range(len(sommets)):
        new_edges = select_closest_in_cone(p_idx, sommets, theta_k)
        for u, v in new_edges:
            all_edges.add((min(u, v), max(u, v)))

    theta_edges = list(all_edges)

def positions_changed():
    """
    Vérifie si les positions des sommets ont changé par rapport à la dernière fois.
    """
    sommets = ic.sommets
    if len(sommets) != len(last_positions):
        return True
    for (x1, y1), (x2, y2) in zip(sommets, last_positions):
        if x1 != x2 or y1 != y2:
            return True
    return False

def is_connected(idx1, idx2):
    """
    Vérifie si deux sommets sont connectés dans le Theta Graph.
    Rebuild automatique si nécessaire.
    """
    if len(ic.sommets) != last_n_points or positions_changed():
        rebuild_theta_edges()

    return (min(idx1, idx2), max(idx1, idx2)) in theta_edges