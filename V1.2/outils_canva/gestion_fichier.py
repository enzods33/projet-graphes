from tkinter import filedialog, messagebox
import json

def sauvegarder_graphe(type_graphe, parametres, points, facteur_global):    
    """
    Sauvegarde l'état du graphe dans un fichier JSON.
    """
    afficher_specification(type_operation="sauvegarde")

    data = {
        "type": type_graphe,
        "facteur_global": facteur_global,
        "parametres": parametres,
        "points": points
    }

    filepath = filedialog.asksaveasfilename(
        defaultextension=".json",
        filetypes=[("Fichiers JSON", "*.json")],
        title="Sauvegarder votre graphe"
    )

    if filepath:
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)
        messagebox.showinfo("Succès", f"Graphe sauvegardé dans {filepath}")

def charger_graphe():
    """
    Charge un fichier JSON et retourne (type_graphe, facteur_global, parametres, points).
    """
    afficher_specification(type_operation="chargement") 

    filepath = filedialog.askopenfilename(
        filetypes=[("Fichiers JSON", "*.json")],
        title="Charger un graphe"
    )

    if not filepath:
        return None, None, None, None

    with open(filepath, "r") as f:
        data = json.load(f)

    type_graphe = data.get("type")
    facteur_global = data.get("facteur_global", 1.0)
    parametres = data.get("parametres", {})
    points = data.get("points", [])
    
    return type_graphe, facteur_global, parametres, points

def afficher_specification(type_operation="chargement"):
    """
    Affiche à l'utilisateur le format attendu pour la sauvegarde ou le chargement d'un graphe.
    """
    if type_operation == "sauvegarde":
        titre = "Spécification du fichier (sauvegarde)"
        message = (
            "Le fichier sera enregistré au format JSON suivant :\n\n"
            "- 'type' : nom du graphe (ex: 'Unit Disk Graph')\n"
            "- 'parametres' : dictionnaire de réglages\n"
            "- 'points' : liste de coordonnées [x, y]\n\n"
            "Exemple :\n"
            "{\n"
            "  'type': 'Unit Disk Graph',\n"
            "  'parametres': {'rayon': 120},\n"
            "  'points': [[100, 200], [300, 400]]\n"
            "}"
        )
    else:
        titre = "Spécification du fichier (chargement)"
        message = (
            "Le fichier JSON doit contenir :\n\n"
            "- 'type' : nom du graphe\n"
            "- 'parametres' : dictionnaire de réglages\n"
            "- 'points' : liste de coordonnées [x, y]"
        )

    messagebox.showinfo(titre, message)