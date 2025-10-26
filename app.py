#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import appui as baseui


class app(baseui.appUI):
    def __init__(self, master=None):
        super().__init__(master)

    def salvar(self):
        pass

    def atualizar(self):
        pass

    def excluir(self):
        pass

    def limpar(self):
        pass


if __name__ == "__main__":
    app = app()
    app.run()
