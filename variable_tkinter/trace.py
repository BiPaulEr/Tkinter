import tkinter as tk

def afficher_message(*args):
    print(args)
    print("Texte mis à jour :", var_texte.get())

fenetre = tk.Tk()
var_texte = tk.StringVar()

var_texte.trace_add("write", afficher_message)
var_texte.trace_add("read", afficher_message) 

entry_widget = tk.Entry(fenetre, textvariable=var_texte)
entry_widget.pack()

label_widget = tk.Label(fenetre, textvariable=var_texte)
label_widget.pack()

fenetre.mainloop()
