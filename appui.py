#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk

from banco import inserir_dados, listar_dados


def i18n_translator_noop(value):
    """i18n - Setup translator in derived class file"""
    return value


def first_object_callback_noop(widget):
    """on first objec callback - Setup callback in derived class file."""
    pass


def image_loader_default(master, image_name: str):
    """Image loader - Setup image_loader in derived class file."""
    img = None
    try:
        img = tk.PhotoImage(file=image_name, master=master)
    except tk.TclError:
        pass
    return img


class appUI:
    def __init__(
        self,
        master=None,
        *,
        translator=None,
        on_first_object_cb=None,
        data_pool=None,
        image_loader=None        
    ):
        if translator is None:
            translator = i18n_translator_noop
        _ = translator  # i18n string marker.
        if image_loader is None:
            image_loader = image_loader_default
        if on_first_object_cb is None:
            on_first_object_cb = first_object_callback_noop
        # build ui
        tk1 = tk.Tk(master)
        tk1.configure(height=200, width=200)
        # First object created
        on_first_object_cb(tk1)

        frame1 = ttk.Frame(tk1)
        frame1.configure(height=200, width=200)
        self.lbl_data = ttk.Label(frame1, name="lbl_data")
        self.lbl_data.configure(text='Data:')
        self.lbl_data.grid(column=0, padx=5, pady=5, row=0)
        self.lbl_consumo = ttk.Label(frame1, name="lbl_consumo")
        self.lbl_consumo.configure(text='Consumo:')
        self.lbl_consumo.grid(column=0, padx=5, pady=5, row=1)
        self.lbl_injecao = ttk.Label(frame1, name="lbl_injecao")
        self.lbl_injecao.configure(text='Injeção:')
        self.lbl_injecao.grid(column=0, padx=5, pady=5, row=2)
        self.entry_data = ttk.Entry(frame1, name="entry_data")
        self.entry_data.grid(column=1, row=0)
        self.entry_consumo = ttk.Entry(frame1, name="entry_consumo")
        self.entry_consumo.grid(column=1, row=1)
        self.entry_injecao = ttk.Entry(frame1, name="entry_injecao")
        self.entry_injecao.grid(column=1, row=2)
        frame1.pack(pady=10, side="top")
        frame2 = ttk.Frame(tk1)
        frame2.configure(height=200, width=200)
        self.btn_salvar = ttk.Button(frame2, name="btn_salvar")
        self.btn_salvar.configure(text='Salvar')
        self.btn_salvar.grid(column=0, padx=5, row=0)
        self.btn_salvar.configure(command=self.salvar)
        self.btn_atualizar = ttk.Button(frame2, name="btn_atualizar")
        self.btn_atualizar.configure(text='Atualizar')
        self.btn_atualizar.grid(column=1, padx=5, row=0)
        self.btn_atualizar.configure(command=self.atualizar)
        self.btn_excluir = ttk.Button(frame2, name="btn_excluir")
        self.btn_excluir.configure(text='Excluir')
        self.btn_excluir.grid(column=2, padx=5, row=0)
        self.btn_excluir.configure(command=self.excluir)
        self.btn_limpar = ttk.Button(frame2, name="btn_limpar")
        self.btn_limpar.configure(text='Limpar')
        self.btn_limpar.grid(column=3, padx=5, row=0)
        self.btn_limpar.configure(command=self.limpar)
        frame2.pack(pady=10, side="top")
        frame4 = ttk.Frame(tk1)
        frame4.configure(height=200, width=200)

        colunas = ("Data","Consumo","Injeção", "Resultado")
        self.tabela = ttk.Treeview(frame4, columns=colunas, show="headings")

        for coluna in colunas:
            self.tabela.heading(coluna,text=coluna)
            self.tabela.column(coluna,width=100,anchor="center")

        self.tabela.configure(selectmode="extended")
        self.tabela.pack(expand=True, fill="both", side="top")
        frame4.pack(expand=True, fill="both", padx=10, pady=10, side="top")
        
        # Main widget
        self.mainwindow = tk1

        self.carregar_tabela()

    def run(self):
        self.mainwindow.mainloop()

    def salvar(self):
        data = self.entry_data.get()
        consumo = self.entry_consumo.get()
        injecao = self.entry_injecao.get()

        inserir_dados(data,consumo,injecao)

        

    def atualizar(self):
        pass

    def excluir(self):
        pass

    def limpar(self):
        pass

    def carregar_tabela(self):
        for item in self.tabela.get_children():
            self.tabela.delete(item)
        for dado in listar_dados():
            self.tabela.insert("", tk.END, values=(dado["data"],dado["consumo"],dado["injecao"],dado["resultado"]))

if __name__ == "__main__":
    app = appUI()
    app.run()
    
