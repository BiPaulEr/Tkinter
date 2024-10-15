import tkinter as tk

fenetre = tk.Tk()

label1 = tk.Label(fenetre, text="Label tk.TOP fill X", bd=5, relief="solid")  # Bordure solide
label2 = tk.Label(fenetre, text="Label tk.LEFT fill Y", bd=5, relief="solid")
label3 = tk.Label(fenetre, text="Label tk.BOTTOM expand", bd=5, relief="solid")
label4 = tk.Label(fenetre, text="Label tk.BOTTOM", bd=5, relief="solid")

label1.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
label2.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
label3.pack(side=tk.BOTTOM, expand=True, padx=10, pady=10)
label4.pack(side=tk.BOTTOM, expand=False, padx=10, pady=10)*

fenetre.mainloop()
