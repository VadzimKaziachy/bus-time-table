import tkinter as tk
from tkinter import ttk
from tkinter import W, EXTENDED, LEFT, Y, E, END
from typing import NoReturn


class ViewFrame(tk.Frame):

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

        self.update_button = tk.Button(master=self, text='Update', command=self.update_bus, width=52)
        self.search_button = tk.Button(master=self, text='Search', command=self.search_bus)
        self.top_button = tk.Button(master=self, text='Top', command=self.top_bus)
        self.bottom_button = tk.Button(master=self, text='Bottom', command=self.bottom_bus)

        self.search_entry = tk.Entry(master=self, width=32)

    def _init_params_widget(self) -> NoReturn:
        """
        The definition of widget parameters should occur here.
        """
        self.update_button.grid(column=0, row=0, columnspan=4)

        self.search_entry.grid(column=0, row=1, columnspan=3)

        self.search_button.grid(column=0, row=2)
        self.top_button.grid(column=1, row=2)
        self.bottom_button.grid(column=2, row=2)

        self.list_box_frame.grid(column=3, row=1, rowspan=2, sticky=E)
        self.list_box.pack(side=LEFT)
        self.list_box.config(yscrollcommand=self.scroll.set)

        self.scroll.pack(side=LEFT, fill=Y)

    def search_bus(self) -> NoReturn:
        """
        The method is designed to search for buses by bus stop.
        """
        self.list_box.delete(first=0, last=END)

        buses = self.service.get_buses_by_point(point=self.search_entry.get())
        for bus in buses:
            self.list_box.insert(END, bus.route_number)

    def top_bus(self) -> NoReturn:
        """
        The method is designed to sort buses from larger to smaller.
        """
        self.list_box.delete(first=0, last=END)

        buses = self.service.sort_buses(reverse=True)
        for bus in buses:
            self.list_box.insert(END, bus.route_number)

    def bottom_bus(self) -> NoReturn:
        """
        The method is designed to sort buses from smaller to larger.
        """
        self.list_box.delete(first=0, last=END)

        buses = self.service.sort_buses(reverse=False)
        for bus in buses:
            self.list_box.insert(END, bus.route_number)

    def update_bus(self) -> NoReturn:
        """
        The method is necessary to get the path to the file and save it in the service.
        """
        self.list_box.delete(first=0, last=END)

        buses = self.service.repository.buses
        for bus in buses:
            self.list_box.insert(END, bus.route_number)
