import tkinter as tk
from interface_graphique.menu import ouvrir_menu

def main():
    """
    Lance l'application principale du projet.

    Initialise la fenêtre principale Tkinter,
    configure ses dimensions et son titre, puis affiche
    le menu principal avec les options de sélection de graphe.

    Elle termine en lançant la boucle principale Tkinter (mainloop),
    qui permet de gérer les événements utilisateur.

    À appeler uniquement si ce fichier est exécuté directement.
    """
    root = tk.Tk()
    root.title("Projet Graphe")
    root.geometry("800x600")
    
    ouvrir_menu(root)
    root.mainloop()

if __name__ == "__main__":
    main()