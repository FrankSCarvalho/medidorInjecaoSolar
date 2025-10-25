import tkinter as tk
from tkinter import ttk, messagebox

class Aplicativo:
    def __init__(self):
        # Criar a janela principal
        self.janela = tk.Tk()
        self.janela.title("Gerenciamento de Energia Solar")
        self.janela.geometry("600x400")
        
        # Criar os widgets
        self.criar_widgets()
        
    def criar_widgets(self):
        # Frame principal
        self.frame_principal = ttk.Frame(self.janela, padding="10")
        self.frame_principal.pack(fill=tk.BOTH, expand=True)
        

        # Label
        self.label = ttk.Label(self.frame_principal, text="Gerenciamento de Energia Solar")
        self.label.grid(column=0, row=0, columnspan=2)

        # Label Consumo
        self.lblConsumo = ttk.Label(self.frame_principal, text="Consumo (KWh):")
        self.lblConsumo.grid(column=0, row=1, padx=10, pady=10)
        
        # Entry Consumo
        self.entryConsumo = ttk.Entry(self.frame_principal)
        self.entryConsumo.grid(column=1, row=1, padx=10, pady=10)

        # Label Injetada
        self.lblInjetada = ttk.Label(self.frame_principal, text="Energia Injetada (KWh):")
        self.lblInjetada.grid(column=0, row=2, padx=10, pady=10)
        
        # Entry Injetada
        self.entryInjetada = ttk.Entry(self.frame_principal)
        self.entryInjetada.grid(column=1, row=2, padx=10, pady=10)
        
        # Botão
        self.botao = ttk.Button(
            self.frame_principal, 
            text="Clique Aqui", 
            command=self.ao_clicar_botao
        )
        self.botao.grid(column=1,row=3,pady=5)
        
        # Listbox
        self.listbox = tk.Listbox(self.frame_principal, height=10)
        self.listbox.grid(column=0, row=4, columnspan=2)
        
    def ao_clicar_botao(self):
        texto = self.entry.get()
        if texto:
            self.listbox.insert(tk.END, texto)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Digite algo no campo de texto!")
    
    def executar(self):
        self.janela.mainloop()

# Executar o aplicativo
if __name__ == "__main__":
    app = Aplicativo()
    app.executar()