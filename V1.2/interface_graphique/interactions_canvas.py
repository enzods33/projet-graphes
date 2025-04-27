import tkinter as tk
from outils_canva import fonction_math as fm

sommets = []
canva = None
point_deplace = None
derniere_pos_souris = None
click_start_time = None
click_start_pos = None
label_compteur = None

callbacks = {
    "click": None,
    "reset": None,
    "update_edges": None,
    "is_connected": None,
    "get_parametres": None,
    "set_parametres": None,
    "get_type_graphe": None  
}

def set_label_compteur(label):
    """
    Définit le label Tkinter utilisé pour afficher le compteur de sommets/arêtes.
    """
    global label_compteur
    label_compteur = label
    update_compteur()

def update_compteur():
    if label_compteur and canva:
        nb_sommets = len(sommets)
        nb_aretes = 0
        for i in range(len(sommets)):
            for j in range(i+1, len(sommets)):
                if callbacks.get("is_connected"):
                    if callbacks["is_connected"](sommets[i], sommets[j]):
                        nb_aretes += 1
        label_compteur.config(text=f"Sommets : {nb_sommets} | Arêtes : {nb_aretes}")

def set_canvas(canvas):
    """
    Définit le canvas Tkinter utilisé globalement pour les interactions.

    Paramètres :
        canvas : objet Tkinter Canvas sur lequel tout sera dessiné.
    """
    global canva
    canva = canvas

def reset():
    """
    Réinitialise le canvas et la liste des sommets.
    Supprime tous les éléments visuels du canvas et appelle le callback reset spécifique s'il existe.
    """
    global sommets
    sommets.clear()
    if canva:
        canva.delete("all")
    if callbacks.get("reset"):
        callbacks["reset"]()
    update_compteur()

def enregistrer_callback_get_type_graphe(func):
    """
    Enregistre une fonction qui retourne le type du graphe courant sous forme de string.
    """
    callbacks["get_type_graphe"] = func

def enregistrer_callback_get_parametres(func):
    callbacks["get_parametres"] = func

def enregistrer_callback_set_parametres(func):
    callbacks["set_parametres"] = func

def enregistrer_callback_is_connected(func):
    """
    Enregistre une fonction qui détermine si deux sommets sont connectés selon le type de graphe.
    """
    callbacks["is_connected"] = func

def enregistrer_callback_click(func):
    """
    Enregistre une fonction à appeler lors d'un clic simple sur le canvas.
    """
    callbacks["click"] = func

def enregistrer_callback_reset(func):
    """
    Enregistre une fonction de réinitialisation spécifique au graphe utilisé.
    """
    callbacks["reset"] = func

def enregistrer_callback_update_edges(func):
    """
    Enregistre une fonction qui sera appelée à chaque fois que les sommets sont déplacés
    ou modifiés, afin de recalculer et redessiner les arêtes.

    Paramètres :
        func : fonction callback à appeler.
    """
    callbacks["update_edges"] = func

def create_point(x, y):
    """
    Crée un point visuel sur le canvas aux coordonnées données.

    Le point est représenté par un petit carré jaune.

    Paramètres :
        x : abscisse du point
        y : ordonnée du point

    Retour :
        Identifiant du rectangle créé sur le canvas.
    """
    point= canva.create_rectangle(x-3, y-3, x+3, y+3, fill="yellow")
    update_compteur()
    return  point

def on_right_click(event):
    """
    Gère le clic droit sur un point existant.

    Supprime le point le plus proche du clic (s'il existe)
    ainsi que les arêtes qui lui sont connectées.

    Paramètres :
        event : événement Tkinter contenant les coordonnées du clic.
    """
    click_coords = (event.x, event.y)
    target = fm.find_closest_point(click_coords, sommets, canva.coords)
    if target is not None:
        remove_edges(target)
        canva.delete(target)
        sommets.remove(target)
    update_compteur()

def remove_edges(sommet):
    """
    Supprime toutes les arêtes (lignes) connectées à un sommet donné.

    Paramètres :
        sommet : identifiant du point dont on veut retirer les arêtes.
    """
    point_coords = canva.coords(sommet)
    items = canva.find_all()
    for item in items:
        if canva.type(item) == "line" and fm.is_connected(canva.coords(item), point_coords):
            canva.delete(item)
    update_compteur()

def is_drag(event):
    """
    Détecte si le clic gauche est sur un point existant, auquel cas on initie un drag.

    Sinon, appelle un éventuel callback de clic pour ajouter un point.

    Paramètres :
        event : événement Tkinter contenant les coordonnées du clic.
    """
    for point in sommets:
        x1, y1, x2, y2 = canva.coords(point)
        if x1 <= event.x <= x2 and y1 <= event.y <= y2:
            on_drag_start(event, point)
            return

    if callbacks["click"]:
        callbacks["click"](event)
    if callbacks["update_edges"]:
        callbacks["update_edges"]()

        
def on_drag_start(event, point):
    """
    Initialise le déplacement d'un point par glisser-déposer.

    Mémorise la position de départ et le point sélectionné.

    Paramètres :
        event : événement de clic
        point : identifiant du point sélectionné
    """
    global point_deplace, derniere_pos_souris
    point_deplace = point
    derniere_pos_souris = (event.x, event.y) 

def on_drag_motion(event):
    """
    Met à jour la position d'un point pendant son déplacement (drag).

    Déplace le point sur le canvas et met à jour les arêtes si un callback est enregistré.

    Paramètres :
        event : événement de mouvement de la souris
    """
    global point_deplace, derniere_pos_souris
    if point_deplace is not None:
        dx = event.x - derniere_pos_souris[0]
        dy = event.y - derniere_pos_souris[1]
        canva.move(point_deplace, dx, dy)
        derniere_pos_souris = (event.x, event.y)
        if callbacks["update_edges"]:
            callbacks["update_edges"]()

def on_drag_end(event):
    """
    Termine le déplacement d'un point. Réinitialise l'état du drag and drop.

    Paramètres :
        event : événement de relâchement du bouton de souris
    """
    global point_deplace
    if point_deplace is not None:
        point_deplace = None

def changer_graphe(frame_actuel, root):
    """
    Détruit l'interface actuelle et ouvre le menu principal pour changer de graphe.

    Appelle les fonctions de reset global et spécifique, puis relance le menu.

    Paramètres :
        frame_actuel : conteneur Tkinter actuel à supprimer
        root : fenêtre principale de l'application
    """
    reset()  # Réinitialisation générique
    if callbacks["reset"]:
        callbacks["reset"]()  # Reset spécifique au graphe (ex: remettre le rayon)
    frame_actuel.destroy()

    from interface_graphique.ui.menu_principal import ouvrir_menu
    ouvrir_menu(root)

def couples_som():
    """
    (À compléter) Devrait renvoyer une liste de couples de sommets connectés.

    Actuellement non implémentée.
    """
    pass

def appliquer_parametres_si_disponible(parametres):
    """
    Applique les paramètres au graphe courant si un callback set_parametres est enregistré.
    """
    if parametres and callbacks.get("set_parametres"):
        callbacks["set_parametres"](parametres)
    if callbacks.get("update_edges"):
        callbacks["update_edges"]()
