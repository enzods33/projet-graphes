"""
Module pour la gestion des fichiers de points 2D.

Ce module permet de :
- lire un fichier texte contenant des coordonnées (x y),
- sauvegarder des listes de points dans un fichier,
- charger des points depuis un fichier avec sélection par l'utilisateur.

Les fichiers doivent contenir une ligne par point : x y
Les lignes vides ou commençant par '#' sont ignorées.
"""
from tkinter import filedialog, messagebox
import json

def sauvegarder_graphe(type_graphe, parametres, points):
    """
    Sauvegarde l'état du graphe dans un fichier JSON.
    """
    afficher_specification(type_operation="sauvegarde")  # ➔ Ajout du message explicatif

    data = {
        "type": type_graphe,
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

def charger_graphe(callback_chargement):
    """
    Charge un fichier JSON et exécute le callback fourni avec type, paramètres et points.
    """
    afficher_specification(type_operation="chargement")  # ➔ Ajout du message explicatif

    filepath = filedialog.askopenfilename(
        filetypes=[("Fichiers JSON", "*.json")],
        title="Charger un graphe"
    )

    if filepath:
        with open(filepath, "r") as f:
            data = json.load(f)

        type_graphe = data.get("type")
        parametres = data.get("parametres", {})
        points = data.get("points", [])

        callback_chargement(type_graphe, parametres, points)

def afficher_specification(type_operation="chargement"):
    """
    Affiche à l'utilisateur le format attendu pour la sauvegarde ou le chargement d'un graphe.

    Paramètres :
        type_operation : "sauvegarde" ou "chargement"
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
            "- 'type' : nom du graphe (ex: 'Unit Disk Graph')\n"
            "- 'parametres' : dictionnaire de réglages\n"
            "- 'points' : liste de coordonnées [x, y]\n\n"
            "Assurez-vous que le fichier respecte cette structure pour éviter les erreurs."
        )

    messagebox.showinfo(titre, message)