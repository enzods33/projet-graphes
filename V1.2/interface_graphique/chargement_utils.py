from interface_graphique import interactions_canvas as ic
from outils_canva.constantes import SCROLLX1, SCROLLX2, SCROLLY1, SCROLLY2

def appliquer_etat_graphe(points, facteur_global, parametres=None):
    """
    Recharge complètement un graphe :
    - reset le canvas
    - crée les points
    - applique le facteur de zoom
    - applique les paramètres spécifiques
    """
    ic.reset()

    for x, y in points:
        point = ic.create_point(x, y)
        ic.sommets.append(point)

    ic.appliquer_facteur_global_initial(facteur_global)

    ic.appliquer_parametres_si_disponible(parametres)

    ic.corriger_taille_points_apres_scale(facteur_global)
    ic.reafficher_les_aretes()
