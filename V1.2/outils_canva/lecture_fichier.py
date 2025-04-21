"""
Module pour lire un fichier texte contenant des points 2D.

Chaque ligne doit contenir deux valeurs numériques séparées par un espace.
Les lignes vides ou commençant par '#' sont ignorées.
"""

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