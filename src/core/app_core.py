import tkinter as tk
from tkinter import ttk

from typing import NoReturn

from frames.view_frame import ViewFrame
from frames.edit_frame import EditFrame
from frames.upload_frame import UploadFrame
from services.bus_service import BusService

from tkinter import messagebox as mb


class AppCore:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title('BusStop')
        self.window.geometry('450x250')
        self.window.resizable(False, False)

        self.bus_service = BusService()

        self.tab_control = ttk.Notebook(self.window)

        self.edit_frame = EditFrame(master=self.tab_control, service=self.bus_service)
        self.upload_frame = UploadFrame(master=self.tab_control, service=self.bus_service)
        self.view_frame = ViewFrame(master=self.tab_control, service=self.bus_service)

        self.tab_control.add(self.upload_frame, text='Upload')
        self.tab_control.add(self.edit_frame, text='Edit')
        self.tab_control.add(self.view_frame, text='View')

        self.tab_control.pack(expand=1, fill='both')

        self.window.protocol("WM_DELETE_WINDOW", self._ask_quit)

        self._center_windows()

    def start_core(self) -> NoReturn:
        """
        The method is intended to launch the application.
        """
        self.window.mainloop()

    def _ask_quit(self) -> NoReturn:
        """
        The method is intended for saving data to a file.
        """
        answer = mb.askyesno(title="Question", message="Save data?")
        if answer:
            self.bus_service.save_in_file()
        self.window.destroy()

    def _center_windows(self):
        """
        The method is designed to center the window.
        """
        x = (self.window.winfo_screenwidth() - self.window.winfo_reqwidth()) / 2.5
        y = (self.window.winfo_screenheight() - self.window.winfo_reqheight()) / 2.5
        self.window.wm_geometry("+%d+%d" % (x, y))
        self.window.mainloop()