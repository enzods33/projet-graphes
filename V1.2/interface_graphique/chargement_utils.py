from interface_graphique import interactions_canvas as ic
from outils_canva.constantes import SCROLLX1, SCROLLX2, SCROLLY1, SCROLLY2, CANVAS_HAUTEUR, CANVAS_LARGEUR

def appliquer_etat_graphe(points, facteur_global, parametres=None, scroll_x=0, scroll_y=0):
    """
    Recharge complètement un graphe :
    - reset le canvas
    - crée les points
    - applique le facteur de zoom
    - applique les paramètres spécifiques
    - repositionne la vue si besoin
    """
    ic.reset()

    # Créer les points avec facteur_global appliqué
    for x, y in points:
        point = ic.create_point(x * facteur_global, y * facteur_global)
        ic.sommets.append(point)

    ic.apply_intial_global_factor(facteur_global)
    ic.apply_parameters_if_posible(parametres)
    ic.update_edge()

    # Appliquer ensuite la position de scroll sauvegardée
    if scroll_x != 0:
        ic.canva.xview_scroll(scroll_x, "units")
    if scroll_y != 0:
        ic.canva.yview_scroll(scroll_y, "units")

    # Mettre à jour les compteurs internes
    ic.unite_scroll_x = scroll_x
    ic.unite_scroll_y = scroll_y
