import tkinter as tk

fenetre = tk.Tk()
var_texte = tk.StringVar()

entry_widget = tk.Entry(fenetre, textvariable=var_texte)
entry_widget.pack()

label = tk.Label(fenetre, textvariable=var_texte)
label.pack()

fenetre.mainloop()
