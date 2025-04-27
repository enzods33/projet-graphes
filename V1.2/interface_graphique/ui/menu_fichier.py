import tkinter as tk

import interface_graphique.interactions_canvas as ic
import outils_canva.geometrie as geo
from outils_canva.gestion_fichier import sauvegarder_graphe, charger_graphe

def ajouter_menu_fichier(root):
    """
    Ajoute un menu 'Fichier' pour sauvegarder et charger depuis l'interface graphique.
    """
    menubar = tk.Menu(root)
    menu_fichier = tk.Menu(menubar, tearoff=0)

    menu_fichier.add_command(label="Sauvegarder Graphe", command=action_sauvegarder_graphe)
    menu_fichier.add_command(label="Charger Graphe", command=action_charger_graphe)

    menubar.add_cascade(label="Fichier", menu=menu_fichier)
    root.config(menu=menubar)

def action_sauvegarder_graphe():
    """
    Sauvegarde le graphe actuel (type, paramètres et points) dans un fichier JSON.
    """
    # Récupération du type, des points et des paramètres
    type_graphe = ic.callbacks["get_type_graphe"]()
    points = [geo.get_center(ic.canva.coords(point)) for point in ic.sommets]

    # Vérification si des paramètres sont disponibles
    if ic.callbacks.get("get_parametres"):
        parametres = ic.callbacks["get_parametres"]()
    else:
        parametres = {}

    # Sauvegarde dans le fichier avec le format JSON
    sauvegarder_graphe(type_graphe, parametres, points)

def action_charger_graphe():
    """
    Charge un fichier JSON de graphe et applique les données.
    """
    def callback_chargement(type_graphe, parametres, points):
        """
        Callback qui est appelé une fois le fichier JSON chargé.
        Applique les points et les paramètres du graphe.
        """
        ic.reset()

        # Création des points sur le canvas
        for x, y in points:
            point = ic.create_point(x, y)
            ic.sommets.append(point)

        # Appliquer les paramètres
        if ic.callbacks.get("set_parametres"):
            ic.callbacks["set_parametres"](parametres)
        
        # Recalcul des arêtes si nécessaire
        if ic.callbacks.get("update_edges"):
            ic.callbacks["update_edges"]()

    # Lancer le chargement du fichier JSON
    charger_graphe(callback_chargement)

