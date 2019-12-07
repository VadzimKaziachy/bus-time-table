import os
import tkinter as tk
from tkinter import ttk

from frames.view_frame import ViewFrame
from frames.edit_frame import EditFrame
from frames.upload_frame import UploadFrame
from services.autobus_service import AutobusService


class AppCore:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Добро пожаловать в приложение PythonRu")
        self.window.geometry('400x250')

        self.autobus_service = AutobusService()

        self.tab_control = ttk.Notebook(self.window)

        self.edit_frame = EditFrame(master=self.tab_control, service=self.autobus_service)
        self.upload_frame = UploadFrame(master=self.tab_control, service=self.autobus_service)

        self.tab_control.add(self.upload_frame, text='Upload')
        self.tab_control.add(self.edit_frame, text='Edit')

        self.tab_control.pack(expand=1, fill='both')

    def start_core(self):
        self.window.mainloop()
