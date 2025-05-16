import tkinter as tk

def create_description_window(root, nom):
    description = descriptions.get(nom)

    fenetre_infos = tk.Toplevel(root)
    fenetre_infos.title(f"Description - {nom}")
    fenetre_infos.geometry("500x400")
    fenetre_infos.configure(bg="#f0f0f0")

    titre = tk.Label(fenetre_infos, text=nom, font=("Helvetica", 20, "bold"), bg="#f0f0f0")
    titre.pack(pady=10)

    label = tk.Label(
        fenetre_infos,
        text=description,
        font=("Helvetica", 20),
        bg="#ffffff",
        wraplength=440,
        justify="center",
        anchor="center"
    )
    label.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)


descriptions = {
    "Delaunay triangulation graph": 
        "La triangulation de Delaunay relie un ensemble de points de sorte qu'aucun point ne se trouve à l'intérieur du cercle circonscrit d'aucun triangle. ",

    "Gabriel graph":
        "Le graphe de Gabriel relie deux points si et seulement si le cercle dont ce segment est le diamètre ne contient aucun autre point. ",
    
    "Integer graph": 
        "Le graphe entier connecte les points dont les coordonnées sont entières.",

    "K closest neighbors graph": 
        "Le graphe k closest neighbors relie chaque point à ses k plus proches voisins. ",

    "Minimum spanning tree graph": 
        "L'arbre couvrant de poids minimal relie tous les points sans former de cycle, avec la longueur totale la plus petite possible. ",

    "Nearest neighbor graph": 
        "Le graphe de plus porche voisin relie chaque point uniquement à son voisin le plus proche. ",

    "Relative neighborhood graph": 
        "Le graphe de voisinage relatif relie deux points seulement si aucun autre point n'est plus proche des deux à la fois. ",

    "Theta graph": 
        "Le graphe theta divise l'espace autour de chaque point en secteurs angulaires, puis connecte le point à celui le plus proche dans chaque secteur. ",

    "Unit disk graph": 
        "Le graphe de disque relie deux points si la distance entre eux est inférieure au rayon choisi. "
    }