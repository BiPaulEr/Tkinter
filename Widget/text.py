import tkinter as tk

def activer():
    text_widget.config(state=tk.NORMAL)

def desactiver():
    text_widget.config(state=tk.DISABLED)

def afficher_texte():
    "1.0 <ligne>.<colonne> == debut ici"
    contenu = text_widget.get("1.0", "end").strip()
    label_texte.config(text=contenu)
    print(contenu)

def annuler():
    text_widget.edit_undo()

fenetre = tk.Tk()
fenetre.title("Activation/Désactivation du Text")

text_widget = tk.Text(fenetre, height=10, width=40, bg="lightyellow", undo=True)
text_widget.pack(padx=10, pady=10)

btn_activer = tk.Button(fenetre, text="Activer Saisie", command=activer)
btn_activer.pack(pady=5)

btn_desactiver = tk.Button(fenetre, text="Désactiver Saisie", command=desactiver)
btn_desactiver.pack(pady=5)

btn_afficher = tk.Button(fenetre, text="Afficher le Texte", command=afficher_texte)
btn_afficher.pack(pady=5)

btn_annuler = tk.Button(fenetre, text="Annuler", command=annuler)
btn_annuler.pack(pady=5)

label_texte = tk.Label(fenetre, text="", bg="lightgray", wraplength=300)  # Label vide au départ
label_texte.pack(pady=10)

fenetre.mainloop()
