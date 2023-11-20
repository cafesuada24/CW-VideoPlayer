from tkinter import *
from tkinter import ttk

from ..namespace import Widgets
from ..events.events import UpdateButtonClickEvent 
from ..events.event_handlers import EventHandler

class UpdateVideoPanel(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=3)

        ttk.Label(self, text='Update Video').grid(row=0, column=0, columnspan=2)
        ttk.Separator(self, orient='horizontal').grid(row=1, column=0, columnspan=2, sticky=NSEW)

        attrs = ('Number', 'Name', 'Director', 'Path')
        for row, attr in zip(range(2, len(attrs) * 2 + 2, 2), attrs):
            ttk.Label(self, text=attr).grid(row=row, column=0, sticky=W)
            input = ttk.Entry(self, width=30).grid(row=row, column=1, ipady=3, sticky=E)
            ttk.Separator(self, orient='horizontal').grid(row=row+1, column=0, columnspan=2, sticky=NSEW)
        button = ttk.Button(self, text='Update', width=20)
        button.grid(row=10, column=1, sticky=E)

        for children in self.winfo_children():
            children.grid(padx=5, pady=5)
