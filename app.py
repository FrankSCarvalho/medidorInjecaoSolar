import tkinter as tk
from tkinter import ttk, messagebox

class Aplicativo:
    def __init__(self):
        # Criar a janela principal
        self.janela = tk.Tk()
        self.janela.title("Meu Aplicativo")
        self.janela.geometry("600x400")
        
        # Criar os widgets
        self.criar_widgets()
        
    def criar_widgets(self):
        # Frame principal
        self.frame_principal = ttk.Frame(self.janela, padding="10")
        self.frame_principal.pack(fill=tk.BOTH, expand=True)
        
        # Label
        self.label = ttk.Label(self.frame_principal, text="Bem-vindo ao Meu App!")
        self.label.pack(pady=10)
        
        # Entry
        self.entry = ttk.Entry(self.frame_principal, width=30)
        self.entry.pack(pady=5)
        
        # Botão
        self.botao = ttk.Button(
            self.frame_principal, 
            text="Clique Aqui", 
            command=self.ao_clicar_botao
        )
        self.botao.pack(pady=5)
        
        # Listbox
        self.listbox = tk.Listbox(self.frame_principal, height=10)
        self.listbox.pack(pady=10, fill=tk.BOTH, expand=True)
        
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