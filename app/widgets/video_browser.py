from collections.abc import Sequence
from tkinter import *
from tkinter import ttk

from ..namespace import Variable

class VideoBrowser(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        columns = ('id', 'name', 'director', 'rating')
        headings = ('ID', 'Name', 'Director', 'Rating')
        columns_width = (50, 300, 300, 150)
        self.__browser = ttk.Treeview(self, show='headings', height=20)
        self.__browser['columns'] = columns
        for col, heading in zip(columns, headings):
            self.__browser.heading(col, text=heading)
        for col, width in zip(columns, columns_width):
            self.__browser.column(col, width=width)
        self.__browser.bind('<<TreeviewSelect>>', self.__item_selected)
        self.__browser.grid(row=0, column=0, sticky=NSEW)
        
         
    def __clear_contents(self):
        for item in self.__browser.get_children():
            self.__browser.delete(item)

    def __item_selected(self, *ignore):
        selected = self.__browser.focus()
        selected = self.__browser.item(selected)['values']
        try:
            Variable.selected_item.set(selected[0])
        except:
            pass

    def display_items(self, contents: Sequence[Sequence]) -> None:
        self.__clear_contents()
        for content in contents:
            _content = (content.id, content.get_name(), content.get_director(), content.get_rating())
            self.__browser.insert('', END, values=_content)


