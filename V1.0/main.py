import fonctions
import tkinter as tk

root = tk.Tk()
root.title("Graphe")
root.geometry("600x400")

distance=150

canva = tk.Canvas(root, width=600, height=400)
canva.pack()

sommets=[]
canva.bind("<Button-1>", lambda event: fonctions.put_point(event, canva, sommets, distance) )  # capture de clic gauche et met un sommet
canva.bind("<Button-3>", lambda event: fonctions.remove_point(event, canva, sommets))  # Clic gauche

canva.mainloop()