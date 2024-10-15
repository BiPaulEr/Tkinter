import tkinter as tk

fenetre = tk.Tk()

label1 = tk.Label(fenetre, text="Label 1 r:0 c:0", bg="lightblue")
label2 = tk.Label(fenetre, text="Label 2 r:0 c:1", bg="lightgreen")
label3 = tk.Label(fenetre, text="Label 3 r:1 c:0 cspan:2", bg="lightcoral")
label4 = tk.Label(fenetre, text="Label 4 r:2 c:0", bg="lightyellow")
label5 = tk.Label(fenetre, text="Label 5 r:2 c:1", bg="lightgray")

label1.grid(row=0, column=0, padx=5, pady=5,  sticky="nsew")
label2.grid(row=0, column=1, padx=5, pady=5,  sticky="nsew")
label3.grid(row=1, column=0, columnspan=2, padx=5, pady=5,  sticky="nsew")
label4.grid(row=2, column=0, padx=5, pady=5,  sticky="nsew")
label5.grid(row=2, column=1, padx=5, pady=5,  sticky="nsew")

fenetre.grid_columnconfigure(0, weight=1)
fenetre.grid_columnconfigure(1, weight=1)
fenetre.grid_rowconfigure(0, weight=1)
fenetre.grid_rowconfigure(1, weight=1)
fenetre.grid_rowconfigure(2, weight=1)

fenetre.mainloop()
