"""
Module utilitaire pour charger des fichiers de points.

Contient une fonction générique pour ouvrir un fichier texte contenant
des coordonnées (x y) et appliquer une action sur la liste des points chargés.
"""

from tkinter import filedialog, messagebox
from outils_canva.lecture_fichier import lire_points_depuis_fichier

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