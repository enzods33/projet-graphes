import tkinter as tk
import interface_graphique.interactions_canvas as ic
from outils_canva.gestion_fichier import sauvegarder_graphe, charger_graphe

def ajouter_menu_fichier(root):
    """
    Ajoute un menu 'Fichier' avec options Sauvegarder et Charger.
    """
    menubar = tk.Menu(root)
    menu_fichier = tk.Menu(menubar, tearoff=0)

    menu_fichier.add_command(label="Sauvegarder Graphe", command=action_sauvegarder_graphe)
    menu_fichier.add_command(label="Charger Graphe", command=action_charger_graphe)

    menubar.add_cascade(label="Fichier", menu=menu_fichier)
    root.config(menu=menubar)

def action_sauvegarder_graphe():
    """
    Sauvegarde l'état actuel du graphe dans un fichier JSON.
    """
    type_graphe = ic.callbacks["get_type_graphe"]()
    facteur_global = ic.facteur_global
    points = [
        ic.coordonnees_reelles[point]
        for point in ic.sommets
    ]

    parametres = ic.callbacks["get_parametres"]() if ic.callbacks.get("get_parametres") else {}

    sauvegarder_graphe(type_graphe, parametres, points, facteur_global)

def action_charger_graphe():
    type_graphe, facteur_global, parametres, points = charger_graphe()

    if type_graphe is None or not points:
        return

    ic.reset()

    # Grouper tout en un dictionnaire
    options = {
        "facteur_global": facteur_global,
        "parametres": parametres,
        "points": points,
    }

    for x, y in options["points"]:
        point = ic.create_point(x, y)
        ic.sommets.append(point)

    ic.appliquer_facteur_global_initial(facteur_global)
    ic.appliquer_parametres_si_disponible(parametres)
    ic.corriger_taille_points_apres_scale(facteur_global)
    ic.reafficher_les_aretes()