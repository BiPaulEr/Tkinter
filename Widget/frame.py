import tkinter as tk

def bouton_clique():
    print("Bouton cliqué dans la première frame !")

fenetre = tk.Tk()
fenetre.title("Exemple avec Deux Frames")

frame1 = tk.Frame(fenetre, borderwidth=2, relief="solid", padx=10, pady=10)
frame1.pack(pady=20, padx=20)

label1 = tk.Label(frame1, text="Label 1 dans la Frame 1", bg="lightblue")
label1.pack(pady=5)

bouton1 = tk.Button(frame1, text="Cliquez-moi", command=bouton_clique)
bouton1.pack(pady=5)

frame2 = tk.Frame(fenetre, borderwidth=2, relief="solid", padx=10, pady=10)
frame2.pack(pady=20, padx=20)

label2 = tk.Label(frame2, text="Label 1 dans la Frame 2", bg="lightgreen")
label2.pack(pady=5)

label3 = tk.Label(frame2, text="Label 2 dans la Frame 2", bg="lightyellow")
label3.pack(pady=5)

fenetre.mainloop()
