"""
Point d'entrée principal de l'application de visualisation de graphes.

Ce module initialise l'interface utilisateur avec Tkinter
et lance le menu principal de sélection des graphes.
"""
import tkinter as tk
from interface_graphique.ui.menu_principal import open_menu
from outils_canva.constantes import ROOT_LARGEUR, ROOT_HAUTEUR, SCROLLX1, SCROLLX2, SCROLLY1, SCROLLY2
from interface_graphique import interactions_canvas as ic

def main():
    root = tk.Tk()
    root.title("Projet Graphe")

    # Taille initiale
    root.geometry(f"{ROOT_LARGEUR}x{ROOT_HAUTEUR}")

    # Taille minimale (facultatif)
    root.minsize(ROOT_LARGEUR, ROOT_HAUTEUR)

    # Autoriser le redimensionnement
    root.resizable(True, True)

    open_menu(root)
    root.mainloop()

if __name__ == "__main__":
    main()