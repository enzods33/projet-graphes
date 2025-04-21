"""
Point d'entrée principal de l'application de visualisation de graphes.

Ce module initialise l'interface utilisateur avec Tkinter
et lance le menu principal de sélection des graphes.
"""
import tkinter as tk
from interface_graphique.ui.menu_principal import ouvrir_menu

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
    root.geometry("800x600")
    
    ouvrir_menu(root)
    root.mainloop()

if __name__ == "__main__":
    main()