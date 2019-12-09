import tkinter as tk
from tkinter import ttk
from tkinter import W, EXTENDED,  LEFT, Y, E, END
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

        self.update_button = tk.Button(master=self, text='Update', command=self.update_bus, width=52)
        self.save_button = tk.Button(master=self, text='Save', command=self.save_bus)
        self.edit_button = tk.Button(master=self, text='Edit', command=self.edit_bus)
        self.delete_button = tk.Button(master=self, text='Delete', command=self.delete_button)

        self.time_label = tk.Label(master=self, text='Time')
        self.final_point_label = tk.Label(master=self, text='Final point')
        self.route_number_label = tk.Label(master=self, text='Route number')
        self.started_point_label = tk.Label(master=self, text='Started point')

        self.time_entry = tk.Entry(master=self, width=20)
        self.final_point_entry = tk.Entry(master=self, width=20)
        self.route_number_entry = tk.Entry(master=self, width=20)
        self.started_point_entry = tk.Entry(master=self, width=20)

    def _init_params_widget(self) -> NoReturn:
        """
        The definition of widget parameters should occur here.
        """
        self.update_button.grid(column=0, row=0, columnspan=4)
        self.edit_button.grid(column=0, row=5)
        self.save_button.grid(column=1, row=5)
        self.delete_button.grid(column=2, row=5)

        self.route_number_label.grid(column=0, row=1, sticky=W)
        self.time_label.grid(column=0, row=2, sticky=W)
        self.started_point_label.grid(column=0, row=3, stick=W)
        self.final_point_label.grid(column=0, row=4, stick=W)

        self.route_number_entry.grid(column=1, row=1, sticky=W, columnspan=2)
        self.time_entry.grid(column=1, row=2, sticky=W,columnspan=2)
        self.started_point_entry.grid(column=1, row=3, sticky=W,columnspan=2)
        self.final_point_entry.grid(column=1, row=4, sticky=W,columnspan=2)

        self.list_box_frame.grid(column=3, row=1, rowspan=5, sticky=E)
        self.list_box.pack(side=LEFT)
        self.list_box.config(yscrollcommand=self.scroll.set)

        self.scroll.pack(side=LEFT, fill=Y)

    def update_bus(self) -> NoReturn:
        """
        The method is necessary to get the path to the file and save it in the service.
        """
        self.list_box.delete(first=0, last=END)

        buses = self.service.repository.buses
        for bus in buses:
            self.list_box.insert(END, bus.route_number)

    def edit_bus(self) -> NoReturn:
        """
        In this method, data is added to the water fields.
        """
        index = int(self.list_box.curselection()[0])
        bus = self.service.get_bus_by_number(index=index)

        self.final_point_entry.insert(index=0, string=bus.final_point)
        self.time_entry.insert(index=0, string=bus.time)
        self.started_point_entry.insert(index=0, string=bus.starting_point)
        self.route_number_entry.insert(index=0, string=bus.route_number)

    def delete_button(self) -> NoReturn:
        """
        The method is designed to deleted element.
        """
        index = self.list_box.curselection()
        if index:
            self.service.delete_bus(index=int(index[0]))
        self.update_bus()

    def save_bus(self) -> NoReturn:
        """
        The method is designed to save element or edit.
        """
        index = self.list_box.curselection()
        if index:
            self.service.edit_bus(
                index=index[0],
                starting_point=self.started_point_entry.get(),
                final_point=self.final_point_entry.get(),
                route_number=self.route_number_entry.get(),
                time=self.time_entry.get()
            )
        else:
            self.service.add_bus(
                starting_point=self.started_point_entry.get(),
                final_point=self.final_point_entry.get(),
                route_number=self.route_number_entry.get(),
                time=self.time_entry.get()
            )
        self._clear_field()
        self.update_bus()

    def _clear_field(self) -> NoReturn:
        """
        The method is designed to clear fields.
        """
        self.started_point_entry.delete(0, END)
        self.final_point_entry.delete(0, END)
        self.route_number_entry.delete(0, END)
        self.time_entry.delete(0, END)
