import tkinter as tk
from tkinter import ttk


class EditFrame(ttk.Frame):

    def __init__(self, master, service):
        super().__init__(master)
        self.master = master
        self.service = service
        lbl1 = tk.Label(self, text='Вкладка 2')
        lbl1.grid(column=0, row=0)

