import tkinter as tk
count = 0
def on_button_click():
    global count
    print("Bouton cliqué !")
    count += 1
    label_resultat.config(text="Vous avez cliqué sur le bouton " + str(count) + " fois.")

def on_button_right_click(event):
    print("Clic droit détecté !")

fenetre = tk.Tk()
fenetre.title("Exemple de Widget Button")

btn_cliquez = tk.Button(fenetre, text="Cliquez-moi", command=on_button_click)
btn_cliquez.pack(pady=10)

btn_cliquez.bind("<Button-3>", on_button_right_click)

label_resultat = tk.Label(fenetre, text="")
label_resultat.pack(pady=10)

fenetre.mainloop()
