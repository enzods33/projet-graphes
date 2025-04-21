import os
import importlib

"""
Parcourt dynamiquement tous les sous-dossiers du dossier 'graphes/' 
et enregistre les fonctions d'ouverture de canvas pour chaque type de graphe.

Chaque sous-dossier doit contenir un fichier '__init__.py' 
exposant une fonction 'ouvrir_canvas' pour que l'import fonctionne.

Exemple :
    graphes_disponibles = {
        "Unit disk graph": <fonction ouvrir_canvas du module unit_disk_graph>,
        ...
    }
"""

graphes_disponibles = {}

# Chemin du dossier actuel (graphes/)
base_path = os.path.dirname(__file__)

# Parcours tous les sous-dossiers
for name in os.listdir(base_path):
    subdir = os.path.join(base_path, name)
    if os.path.isdir(subdir) and not name.startswith("__"):
        module = importlib.import_module(f"{__name__}.{name}")
        nom_affiche = name.replace("_", " ").capitalize()
        graphes_disponibles[nom_affiche] = module.ouvrir_canvas

