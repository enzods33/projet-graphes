"""
Point d'entrée principal de l'application de visualisation de graphes.

Ce module initialise l'interface utilisateur avec Tkinter
et lance le menu principal de sélection des graphes.
"""
import tkinter as tk
from interface_graphique.ui.menu_principal import open_menu
from outils_canva.constantes import ROOT_LARGEUR, ROOT_HAUTEUR, LARGEUR_MIN

def main():
    """
    Lance l'application principale du projet.   

    - Crée la fenêtre principale.
    - Configure le titre et la taille initiale.
    - Affiche le menu principal pour choisir un type de graphe.
    - Démarre la boucle principale Tkinter.
    """
    root = tk.Tk()
    root.title("Projet Graphe")
    root.geometry(f"{ROOT_LARGEUR}x{ROOT_HAUTEUR}")
    root.resizable(True, True)
    root.minsize(LARGEUR_MIN, ROOT_HAUTEUR)
    open_menu(root)
    root.mainloop()

if __name__ == "__main__":
    main()