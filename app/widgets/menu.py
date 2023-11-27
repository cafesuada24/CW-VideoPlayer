import tkinter as tk
from tkinter import ttk

from ..singleton import SingletonMeta
from .abstracts import AppFrame

class Menu(AppFrame, metaclass=SingletonMeta):
    def __init__(self, root):
        super().__init__(root)

        for column in range(3):
            self.columnconfigure(column, weight=1)

    def _create_widgets(self):
        pass
    
    def _display_widgets(self):
        ttk.Label(
            self, text='Select an option by clicking one of the buttons below'
        ).grid(row=0, column=0, columnspan=3)
        ttk.Button(
            self,
            text='Check Videos',
            command=lambda: self._root().display_frame('check_videos'),
        ).grid(row=1, column=0)
        ttk.Button(
            self,
            text='Create Video List',
            command=lambda: self._root().display_frame('create_video_list'),
        ).grid(row=1, column=1)
        ttk.Button(
            self,
            text='Update Videos',
            command=lambda: self._root().display_frame('update_videos'),
        ).grid(row=1, column=2)

        for widget in self.winfo_children():
            widget.grid(padx=5, pady=5, sticky='we')

    def display(self):
        self.grid(row=0, column=0, sticky='nsew')

