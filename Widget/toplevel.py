import tkinter as tk

def ouvrir_fenetre_secondaire():
    fenetre_secondaire = tk.Toplevel(fenetre_principale)
    fenetre_secondaire.title("Fenêtre Secondaire")
    fenetre_secondaire.geometry("300x200")
    fenetre_secondaire.resizable(False, False)

fenetre_principale = tk.Tk()
fenetre_principale.title("Fenêtre Principale")
fenetre_principale.geometry("400x300")
fenetre_principale.config(bg="lightgray")

bouton_ouvrir = tk.Button(fenetre_principale, text="Ouvrir Fenêtre Secondaire", command=ouvrir_fenetre_secondaire)
bouton_ouvrir.pack(pady=10)

fenetre_principale.mainloop()
