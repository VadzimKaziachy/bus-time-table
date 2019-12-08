import tkinter as tk
from tkinter import ttk
from tkinter import W
from tkinter import filedialog as fd
from typing import NoReturn


class EditFrame(ttk.Frame):

    def __init__(self, master, service):
        super().__init__(master)
        self.master = master
        self.service = service

        self._init_widget()
        self._init_params_widget()

    def _init_widget(self) -> NoReturn:
        """
        Widgets must be defined here.
        """
        self.upload_title = tk.Label(self, text='Upload autobus')
        self.upload_button = tk.Button(self, text='Upload', command=self._get_path)

    def _init_params_widget(self) -> NoReturn:
        """
        The definition of widget parameters should occur here.
        """
        self.upload_title.grid(column=0, row=0, sticky=W, padx=150, pady=30)
        self.upload_button.grid(column=0, row=1)

    def _get_path(self):
        """
        The method is necessary to get the path to the file and save it in the service.
        """
        self.upload_title.configure(text=self.service.path)
