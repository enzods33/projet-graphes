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
