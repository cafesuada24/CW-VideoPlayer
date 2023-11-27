import tkinter as tk
from tkinter import ttk

from ..singleton import SingletonMeta


class Footer(ttk.Frame, metaclass=SingletonMeta):
    def __init__(self, root):
        super().__init__(root)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.__back_btn = ttk.Button(self, text='Back', command=self.__back)

        ttk.Label(self, text='Version 1.2').grid(row=0, column=1, sticky='e')
        self.__back_btn.grid(row=0, column=0, sticky='w')

    def __back(self):
        self._root().display_frame('main')
