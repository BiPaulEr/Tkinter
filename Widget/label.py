import tkinter as tk
import os

fenetre = tk.Tk()
fenetre.title("Exemple de Widget Label avec Différentes Options")

label1 = tk.Label(fenetre, text="Label 1: Texte avec fond bleu", bg="lightblue", fg="black", font=("Arial", 14))
label1.pack(pady=5)

label2 = tk.Label(fenetre, text="Label 2: Texte centré", bg="lightgreen", fg="black", font=("Arial", 14), justify=tk.CENTER)
label2.pack(pady=5)

image = tk.PhotoImage(file=os.path.dirname(__file__) + "\sun.png")
label3 = tk.Label(fenetre, image=image)
label3.pack(pady=5)

label4 = tk.Label(fenetre, text="Label 6: Texte en gras", bg="lightpink", fg="black", font=("Arial", 14, "bold"))
label4.pack(pady=5)

label5 = tk.Label(fenetre, text="Label 7: Texte en italique", bg="lightgray", fg="black", font=("Arial", 14, "italic"))
label5.pack(pady=5)

fenetre.mainloop()
