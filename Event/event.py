import tkinter as tk

def afficher_attributs(event):
    texte = (
        f"x = {event.x}\n"
        f"y = {event.y}\n"
        f"x_root = {event.x_root}\n"
        f"y_root = {event.y_root}\n"
        f"char = {event.char if event.char else 'None'}\n"
        f"keysym = {event.keysym if event.keysym else 'None'}\n"
        f"widget = {event.widget}\n"
        f"type = {event.type}\n"
        f"num = {event.num if hasattr(event, 'num') else 'None'}\n"
        f"state = {event.state}\n"
        f"time = {event.time}\n"
    )
    label_event.config(text=texte)

fenetre = tk.Tk()
fenetre.title("Affichage des attributs d'événement")

label_event = tk.Label(fenetre, text="Interagissez avec la fenêtre !", bg="lightgray", width=40, height=15)
label_event.pack(padx=10, pady=10)

fenetre.bind("<Motion>", afficher_attributs)       
fenetre.bind("<ButtonPress>", afficher_attributs) 
fenetre.bind("<KeyPress>", afficher_attributs)

fenetre.mainloop()
