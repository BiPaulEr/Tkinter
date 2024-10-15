import tkinter as tk

def afficher_texte():
    contenu = entry_widget.get()
    label_resultat.config(text=f"Texte saisi : {contenu}")

def modifier_texte():
    entry_widget.delete(0, tk.END)
    entry_widget.insert(0, "Texte initial")

def activer():
    entry_widget.config(state=tk.NORMAL)

def desactiver():
    entry_widget.config(state=tk.DISABLED)

def set_readonly():
    entry_widget.config(state='readonly')

fenetre = tk.Tk()
fenetre.title("Exemple de Widget Entry")

entry_widget = tk.Entry(fenetre)
entry_widget.pack(pady=10)

btn_afficher = tk.Button(fenetre, text="Afficher le texte", command=afficher_texte)
btn_afficher.pack(pady=5)

btn_modifier = tk.Button(fenetre, text="Modifier le texte", command=modifier_texte)
btn_modifier.pack(pady=5)

btn_activer = tk.Button(fenetre, text="Activer Saisie", command=activer)
btn_activer.pack(pady=5)

btn_desactiver = tk.Button(fenetre, text="Désactiver Saisie", command=desactiver)
btn_desactiver.pack(pady=5)

btn_readonly = tk.Button(fenetre, text="Lire seulement", command=set_readonly)
btn_readonly.pack(pady=5)

label_resultat = tk.Label(fenetre, text="Texte saisi : ")
label_resultat.pack(pady=10)

fenetre.mainloop()
