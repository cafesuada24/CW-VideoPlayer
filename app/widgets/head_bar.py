"""This module contains Headbar widget"""

import tkinter as tk
from tkinter import ttk

from ..singleton import SingletonMeta
from .video_browser import VideoBrowser
from ..namespaces.event_handlers import EventHandlers
from ..namespaces.tk_variable import TkVariable


class HeadBar(ttk.Frame, metaclass=SingletonMeta):
    def __init__(self, root):
        super().__init__(root)

        # configuring layout
        for col in range(6):
            self.columnconfigure(col, weight=1)
        self.columnconfigure(6, weight=2, minsize=200)

        # Create widgets
        self.__list_video_btn = ttk.Button(
            self,
            text='List All Videos',
            command=VideoBrowser().display_playlist,
        )
        self.__sort_by = ttk.OptionMenu(
            self,
            TkVariable().sort_by,
            'ID    ',
            *('ID    ', 'Name  ', 'Author', 'Rating'),
            direction='below'
        )
        self.__sort_order = ttk.OptionMenu(
            self,
            TkVariable().sort_order,
            'Ascending ',
            *('Ascending ', 'Descending')
        )
        self.__search_bar = tk.Entry(
            self, textvariable=TkVariable().search_entry
        )

        # Display widgets
        ttk.Label(self, text='Sort by ').grid(row=0, column=1, sticky='e')
        ttk.Label(self, text='Sort order ').grid(row=0, column=3, sticky='e')
        ttk.Label(self, text='Search ').grid(row=0, column=5, sticky='e')

        self.__list_video_btn.grid(row=0, column=0, sticky='w')
        self.__sort_by.grid(row=0, column=2, sticky='w')
        self.__sort_order.grid(row=0, column=4, sticky='w')
        self.__search_bar.grid(row=0, column=6, sticky='we')
