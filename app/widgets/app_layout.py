import tkinter as tk
from tkinter import ttk

from .. import CONFIG
from ..namespaces.widgets import Widgets
from ..namespaces.tk_variable import TkVariable
from ..namespaces.database import Database as DB

COLUMNS = CONFIG['display']['columns']

class MainLayout(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        Widgets(self)

        # Search engine init
        # _data = []
        # for item in General.data:
        #     _data.extend(((item.get_name().lower(), item.id), (item.get_director().lower(), item.id)))
        
        self._head_bar = None
        self._rpanel = None
        self._footer = None
        self._browser = None

        self.columnconfigure(0, weight=7)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=8)
        self.rowconfigure(2, weight=1)

    def display(self, head_bar=None, browser=None, rpanel=None, footer=None):
        if self._head_bar:
            self._head_bar.grid_forget()
        if self._browser:
            self._browser.grid_forget()
        if self._rpanel:
            self._rpanel.grid_forget()
        if self._footer:
            self._footer.grid_forget()
        self._head_bar = head_bar or Widgets().HEAD_BAR
        self._browser = browser or Widgets().BROWSER
        self._rpanel = rpanel
        self._footer = footer or Widgets().FOOTER
        self.__layout()
        self.grid(row=0, column=0, sticky=tk.NSEW)

    def __layout(self):
        self._head_bar.grid(row=0, column=0, sticky=tk.NSEW)
        self._browser.grid(row=1, column=0, sticky=tk.NSEW)
        self._rpanel.grid(row=0, column=1, rowspan=2, sticky=tk.NSEW)
        self._footer.grid(row=2, column=0, columnspan=2, sticky=tk.NSEW)
        for children in (self._head_bar, self._browser, self._rpanel, self._footer):
            children.grid(padx=5, pady=5)
        
