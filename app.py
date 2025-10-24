from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

style = ttk.Style()

style.configure("Titulo.TLabel", font=("Helvetica", 18, "bold"))

LabelTitulo = ttk.Label(frm, text="Gerenciador solar", style="Titulo.TLabel", padding=10)
LabelTitulo.grid(column=0, row=0, columnspan=2)

labelMarcacao = ttk.Label(frm, text="Marcação", padding=10)
labelMarcacao.grid(column=0, row=1)

entryMarcacao = ttk.Entry(frm)
entryMarcacao.grid(column=1, row=1)

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=10)
root.mainloop()