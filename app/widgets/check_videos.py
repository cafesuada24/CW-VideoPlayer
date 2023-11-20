from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msgbox
from collections.abc import Sequence

from .. import CONFIG
from ..namespace import Widgets
from ..events.event_handlers import EventHandler
from ..events.events import CheckButtonClickEvent
from ..namespace import Variable, General

CONFIG = CONFIG['display']['columns']

class CheckVideosPanel(ttk.Frame):    
    def __init__(self, root):
        super().__init__(root)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)

        ttk.Label(self, text='Video Infomation').grid(row=0, column=0, columnspan=2, sticky=(N, S))
        ttk.Separator(self, orient='horizontal').grid(row=1, column=0, columnspan=2, sticky=NSEW)

        attrs = ('Name', 'Director', 'Rating', 'Play count', 'File path')
        self.__info_text = []
        
        ttk.Label(self, text='ID').grid(row=2, column=0, sticky=W)
        self.__id_input = ttk.Entry(self, textvariable=Variable.selected_item)
        self.__id_input.grid(row=2, column=1, ipady=3, sticky=(W, E))
        ttk.Separator(self, orient='horizontal').grid(row=3, column=0, columnspan=2, sticky=NSEW)

        for row, attr in zip(range(4, len(attrs) * 2 + 2, 2), attrs):
            ttk.Label(self, text=attr).grid(row=row, column=0, sticky=W)
            textbox = Text(self, height=1, width=35)
            textbox['state'] = 'disabled'
            textbox.grid(row=row, column=1, ipady=3, sticky=(W, E))
            self.__info_text.append(textbox)
            ttk.Separator(self, orient='horizontal').grid(row=row+1, column=0, columnspan=2, sticky=NSEW)
        
        self.__check_btn = ttk.Button(self, text='Check Videos', width=20, command=self.__show_info)
        self.__play_btn = ttk.Button(self, text='Play', width=20)
        self.__play_btn.grid(row=13, column=0, columnspan=2, sticky=(W, N, S))
        self.__check_btn.grid(row=13, column=1, sticky=(E, N, S))

        for children in self.winfo_children():
            children.grid(padx=7, pady=7)
    
    def display_info(self, data: Sequence):
        for field, attr in zip(self.__info_text, data):
            field['state'] = 'normal'
            field.delete('1.0', END)
            field.insert('1.0', attr)
            field['state'] = 'disabled'

    def __show_info(self, *ignore):
        try:
            id = Variable.selected_item.get()
            data = General.data[id]
            self.display_info(data.list_all(('name', 'director', 'rating', 'play_count', 'file_path')))
        except:
            msgbox.showerror('Id error', message='Invalid ID')

                            
