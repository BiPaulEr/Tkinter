import tkinter as tk

def clic_gauche(event):
    print("Clic gauche détecté")

def clic_droit(event):
    print("Clic droit détecté")

def double_clic_gauche(event):
    print("Double-clic gauche détecté")

def mouvement_souris(event):
    print(f"Mouvement de la souris à ({event.x}, {event.y})")

def curseur_entre(event):
    print("Le curseur est entré dans le widget")

def curseur_sorti(event):
    print("Le curseur a quitté le widget")

def touche_a(event):
    print("Touche 'a' appuyée")

def redimensionnement(event):
    print(f"Fenêtre redimensionnée à {event.width}x{event.height}")

def touche_entree(event):
    print("Touche Enter appuyée")

fenetre = tk.Tk()
fenetre.title("Détection des événements Tkinter")

label = tk.Label(fenetre, text="Interagissez avec ce label", bg="lightblue", width=30, height=5)
label.pack(padx=10, pady=10)

label.bind("<Button-1>", clic_gauche)     
label.bind("<Button-3>", clic_droit)   
label.bind("<Double-Button-1>", double_clic_gauche) 
label.bind("<Motion>", mouvement_souris) 
label.bind("<Enter>", curseur_entre)     
label.bind("<Leave>", curseur_sorti)         

fenetre.bind("<KeyPress-a>", touche_a)
fenetre.bind("<Return>", touche_entree)       
fenetre.bind("<Configure>", redimensionnement) 

fenetre.mainloop()
