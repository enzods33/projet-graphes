import os
import importlib

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
print(graphes_disponibles)