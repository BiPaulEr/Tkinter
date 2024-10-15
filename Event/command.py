import tkinter as tk

def on_button_click():
    print("Bouton cliqué !")

def on_checkbutton_toggle():
    print(f"Checkbutton {'coché' if var_checkbutton.get() else 'décoché'}")

def on_radiobutton_select():
    print(f"Radiobutton sélectionné : {var_radiobutton.get()}")

def on_spinbox_change():
    print(f"Valeur du Spinbox : {spinbox.get()}")

def on_scale_change(value):
    print(f"Valeur du Scale : {value}")

fenetre = tk.Tk()
fenetre.title("Exemples d'utilisation de 'command'")

bouton = tk.Button(fenetre, text="Cliquez-moi", command=on_button_click)
bouton.pack(pady=10)

var_checkbutton = tk.BooleanVar()
checkbutton = tk.Checkbutton(fenetre, text="Option", variable=var_checkbutton, command=on_checkbutton_toggle)
checkbutton.pack(pady=10)

var_radiobutton = tk.StringVar(value="Option 1")
radiobutton1 = tk.Radiobutton(fenetre, text="Option 1", variable=var_radiobutton, value="Option 1", command=on_radiobutton_select)
radiobutton2 = tk.Radiobutton(fenetre, text="Option 2", variable=var_radiobutton, value="Option 2", command=on_radiobutton_select)
radiobutton1.pack(pady=5)
radiobutton2.pack(pady=5)

spinbox = tk.Spinbox(fenetre, from_=0, to=10, command=on_spinbox_change)
spinbox.pack(pady=10)

scale = tk.Scale(fenetre, from_=0, to=100, orient='horizontal', command=on_scale_change)
scale.pack(pady=10)

fenetre.mainloop()
