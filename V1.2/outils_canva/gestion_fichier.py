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

def lire_points_depuis_fichier(filepath):
    """
    Lit un fichier texte contenant des coordonnées (x y) ligne par ligne.

    Paramètres :
        filepath : chemin vers le fichier texte.

    Retour :
        Liste de tuples (x, y) en float.
    """
    points = []
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            x_str, y_str = line.split()
            x, y = float(x_str), float(y_str)
            points.append((x, y))
    return points

def sauvegarder_points_dans_fichier(points, nom_fichier=None):
    """
    Sauvegarde les coordonnées des points dans un fichier texte.

    Toujours ouvre une boîte pour demander où enregistrer, 
    avec 'nom_fichier' utilisé comme nom par défaut si fourni.
    """
    # Demander où sauvegarder, en utilisant nom_fichier si donné
    nom_fichier_dialogue = filedialog.asksaveasfilename(
        defaultextension=".txt",
        initialfile=nom_fichier if nom_fichier is not None and nom_fichier.strip() else None,   #strip() au cas ou le nom de fichier est de type "  test"
        filetypes=[("Fichier texte", "*.txt")],
        title="Choisir où enregistrer le fichier"
    )

    # Si l'utilisateur a cliqué sur "Annuler", on quitte sans erreur
    if not nom_fichier_dialogue:
        print("❌ Sauvegarde annulée par l'utilisateur.")
        return
    
    with open(nom_fichier_dialogue, "w") as f:
        for x, y in points:
            f.write(f"{x} {y}\n")

def charger_fichier_points(callback):
    """
    Ouvre une boîte de dialogue pour sélectionner un fichier de points (.txt),
    lit les coordonnées et exécute une fonction callback avec la liste des points.

    Le fichier doit contenir une ligne par point : x y
    Les lignes vides ou commençant par '#' sont ignorées.

    Paramètres :
        callback : fonction à appeler avec les points chargés [(x1, y1), (x2, y2), ...]
    """
    messagebox.showinfo(
        "Format attendu",
        "Le fichier doit contenir une ligne par point : x y\n\n"
        "Chaque ligne correspond à un sommet.\n"
        "Exemple :\n120 200\n150.5 180\n\n"
        "Les lignes vides et les lignes commençant par '#' sont ignorées."
    )

    filepath = filedialog.askopenfilename(
        filetypes=[("Fichiers texte", "*.txt")],
        title="Charger un nuage de points"
    )

    # Si l'utilisateur a bien sélectionné un fichier (et pas cliqué sur "Annuler")
    if filepath:
    # Lis les points contenus dans le fichier (liste de tuples (x, y))
        points = lire_points_depuis_fichier(filepath)

    # Appelle la fonction fournie avec les points en argument
        callback(points)

def sauvegarder_etat_graphe(type_graphe, parametres, points):
    """
    Sauvegarde l'état complet du graphe (type, paramètres, points) dans un fichier JSON.
    """
    data = {
        "type": type_graphe,
        "parametres": parametres,
        "points": points
    }

    filepath = filedialog.asksaveasfilename(defaultextension=".json",
                                            filetypes=[("Fichiers JSON", "*.json")])

    if filepath:
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)

def charger_etat_graphe(callback_affichage):
    """
    Charge un fichier JSON contenant un graphe et passe les données à une fonction callback.
    """
    filepath = filedialog.askopenfilename(filetypes=[("Fichiers JSON", "*.json")])

    if filepath:
        with open(filepath, "r") as f:
            data = json.load(f)
        
        type_graphe = data.get("type")
        parametres = data.get("parametres", {})
        points = data.get("points", [])

        callback_affichage(type_graphe, parametres, points)

def afficher_specification(type_operation="chargement"):
    """
    Affiche à l'utilisateur le format de fichier attendu pour la sauvegarde ou le chargement.

    Paramètres :
    - type_operation : "sauvegarde" ou "chargement" (par défaut "chargement")
    """
    if type_operation == "sauvegarde":
        messagebox.showinfo(f"Spécification du fichier ({type_operation})",
            "Le fichier sera enregistré au format JSON suivant :\n\n"
            "- 'type' : nom du graphe (ex: 'Unit Disk Graph')\n"
            "- 'parametres' : dictionnaire des réglages\n"
            "- 'points' : liste de coordonnées [x, y]\n\n"
            "Exemple:\n"
            "{\n"
            "  'type': 'Unit Disk Graph',\n"
            "  'parametres': {'rayon': 120},\n"
            "  'points': [[100, 200], [300, 400]]\n"
            "}"
        )
    else:
        messagebox.showinfo(f"Spécification du fichier ({type_operation})",
            "Le fichier JSON doit contenir :\n\n"
            "- 'type' : nom du graphe (ex: 'Unit Disk Graph')\n"
            "- 'parametres' : dictionnaire des réglages\n"
            "- 'points' : liste de coordonnées [x, y]\n\n"
            "Assurez-vous que le fichier respecte cette structure pour éviter des erreurs."
        )

def sauvegarder_graphe(type_graphe, parametres, points):
    """
    Sauvegarde l'état du graphe dans un fichier JSON.
    """
    afficher_specification(type_operation="sauvegarde")
    
    data = {
        "type": type_graphe,
        "parametres": parametres,
        "points": points
    }
    
    filepath = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Fichiers JSON", "*.json")])
    if filepath:
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)
        messagebox.showinfo("Succès", "Graphe sauvegardé avec succès !")

def charger_graphe(callback_chargement):
    """
    Charge un fichier JSON et exécute le callback fourni avec type, parametres et points.
    """
    afficher_specification()
    filepath = filedialog.askopenfilename(filetypes=[("Fichiers JSON", "*.json")])

    if filepath:
        with open(filepath, "r") as f:
            data = json.load(f)
        
        type_graphe = data.get("type")
        parametres = data.get("parametres", {})
        points = data.get("points", [])

        # Appel du callback avec les 3 paramètres : type_graphe, parametres, points
        callback_chargement(type_graphe, parametres, points)