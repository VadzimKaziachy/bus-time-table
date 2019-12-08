import tkinter as tk
from tkinter import ttk
from tkinter import W, EXTENDED, RIGHT, LEFT, Y, BOTTOM, SINGLE, BROWSE, E, END
from typing import NoReturn


class EditFrame(ttk.Frame):

    def __init__(self, master, service):
        super().__init__(master)
        self.master = master
        self.service = service
        self.list_box_frame = ttk.Frame(master=self)

        self._init_widget()
        self._init_params_widget()

    def _init_widget(self) -> NoReturn:
        """
        Widgets must be defined here.
        """
        self.list_box = tk.Listbox(master=self.list_box_frame, selectmode=EXTENDED)
        self.scroll = tk.Scrollbar(master=self.list_box_frame, command=self.list_box.yview)

        self.update_button = tk.Button(master=self, text='Update', command=self.update_data, width=46)
        self.save_button = tk.Button(master=self, text='Save', command=self.save_bus)
        self.add_button = tk.Button(master=self, text='add', command=self.add_bus)

        self.time_label = tk.Label(master=self, text='Time')
        self.final_point_label = tk.Label(master=self, text='Final point')
        self.route_number_label = tk.Label(master=self, text='Route number')
        self.started_point_label = tk.Label(master=self, text='Started point')

        self.time_entry = tk.Entry(master=self, width=10)
        self.final_point_entry = tk.Entry(master=self, width=10)
        self.route_number_entry = tk.Entry(master=self, width=10)
        self.started_point_entry = tk.Entry(master=self, width=10)

    def _init_params_widget(self) -> NoReturn:
        """
        The definition of widget parameters should occur here.
        """
        self.update_button.grid(column=0, row=0, columnspan=3)
        self.add_button.grid(column=0, row=5)
        self.save_button.grid(column=1, row=5)

        self.route_number_label.grid(column=0, row=1, sticky=W)
        self.time_label.grid(column=0, row=2, sticky=W)
        self.started_point_label.grid(column=0, row=3, stick=W)
        self.final_point_label.grid(column=0, row=4, stick=W)

        self.route_number_entry.grid(column=1, row=1, sticky=W)
        self.time_entry.grid(column=1, row=2, sticky=W)
        self.started_point_entry.grid(column=1, row=3, sticky=W)
        self.final_point_entry.grid(column=1, row=4, sticky=W)

        self.list_box_frame.grid(column=2, row=1, rowspan=5, sticky=E)
        self.list_box.pack(side=LEFT)
        self.list_box.config(yscrollcommand=self.scroll.set)

        self.scroll.pack(side=LEFT, fill=Y)

    def update_data(self):
        """
        The method is necessary to get the path to the file and save it in the service.
        """
        self.list_box.delete(first=0, last=END)

        buses = self.service.repository.buses
        for bus in buses:
            self.list_box.insert(END, bus.route_number)

    def save_bus(self):
        self._clear_field()

    def add_bus(self):
        """
        Data is received and transferred to the service here.
        """
        self.service.add_bus(
            starting_point=self.started_point_entry.get(),
            final_point=self.final_point_entry.get(),
            route_number=self.route_number_entry.get(),
            time=self.time_entry.get()
        )
        self._clear_field()
        self.update_data()

    def _clear_field(self):
        """
        The method is designed to clear fields.
        """
        self.started_point_entry.delete(0, END)
        self.final_point_entry.delete(0, END)
        self.route_number_entry.delete(0, END)
        self.time_entry.delete(0, END)
