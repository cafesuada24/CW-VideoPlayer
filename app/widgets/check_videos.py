from tkinter import *
from tkinter import ttk

from .. import CONFIG
from ..namespace import Widgets
from ..events.event_handlers import EventHandler
from ..events.events import CheckButtonClickEvent


CONFIG = CONFIG['display']['columns']

class CheckVideosPanel(ttk.Frame):    
    def __init__(self, root):
        super().__init__(root)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)

        ttk.Label(self, text='Video Infomation').grid(row=0, column=0, columnspan=2, sticky=(N, S))
        ttk.Separator(self, orient='horizontal').grid(row=1, column=0, columnspan=2, sticky=NSEW)

        attrs = ('Number', 'Name', 'Director', 'Play count', 'File path')
        for row, attr in zip(range(2, len(attrs) * 2 + 2, 2), attrs):
            ttk.Label(self, text=attr).grid(row=row, column=0, sticky=W)
            Text(self, height=1, width=35).grid(row=row, column=1, ipady=3, sticky=(W, E))
            ttk.Separator(self, orient='horizontal').grid(row=row+1, column=0, columnspan=2, sticky=NSEW)

        self.__check_btn = ttk.Button(self, text='Check Videos', width=20)
        self.__play_btn = ttk.Button(self, text='Play', width=20)
        self.__play_btn.grid(row=13, column=0, columnspan=2, sticky=(W, N, S))
        self.__check_btn.grid(row=13, column=1, sticky=(E, N, S))

        for children in self.winfo_children():
            children.grid(padx=7, pady=7)
