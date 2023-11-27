import tkinter as tk
from tkinter import ttk

from ..singleton import SingletonMeta
from .head_bar import HeadBar
from .video_browser import VideoBrowser
from .footer import Footer
from .abstracts import AppFrame


class MainLayout(AppFrame, metaclass=SingletonMeta):
    def __init__(self, root):
        super().__init__(root)

        self.columnconfigure(0, weight=7)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=8)
        self.rowconfigure(2, weight=1)

    def _create_widgets(self):
        self._head_bar = None
        self._rpanel = None
        self._footer = None
        self._browser = None

    def _display_widgets(self):
        pass

    def __relayout(self):
        self._head_bar.grid(row=0, column=0, sticky='nsew')
        self._browser.grid(row=1, column=0, sticky='nsew')
        self._rpanel.grid(row=0, column=1, rowspan=2, sticky='nsew')
        self._footer.grid(row=2, column=0, columnspan=2, sticky='nsew')
        for children in (
            self._head_bar,
            self._browser,
            self._rpanel,
            self._footer,
        ):
            children.grid(padx=5, pady=5)
        pass
    

    def display(self, head_bar=None, browser=None, rpanel=None, footer=None):
        if self._head_bar:
            self._head_bar.grid_forget()
        if self._browser:
            self._browser.grid_forget()
        if self._rpanel:
            self._rpanel.grid_forget()
        if self._footer:
            self._footer.grid_forget()
        self._head_bar = head_bar or HeadBar()
        self._browser = browser or VideoBrowser()
        self._rpanel = rpanel
        self._footer = footer or Footer()
        self.__relayout()
        self.grid(row=0, column=0, sticky=tk.NSEW)
