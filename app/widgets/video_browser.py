from collections.abc import Sequence
from tkinter import *
from tkinter import ttk

class VideoBrowser(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Video Browser
        columns = ('number', 'name', 'director', 'rating')
        headings = ('Number', 'Name', 'Director', 'Rating')
        columns_width = (50, 300, 300, 150)
        self.__browser = ttk.Treeview(self, show='headings', height=20)
        self.__browser['columns'] = columns
        for col, heading in zip(columns, headings):
            self.__browser.heading(col, text=heading)
        for col, width in zip(columns, columns_width):
            self.__browser.column(col, width=width)
        self.__browser.grid(row=0, column=0, sticky=NSEW)
         
    def __clear_contents(self):
        for item in self.__browser.get_children():
            self.__browser.delete(item)

    def display_items(self, contents: Sequence[Sequence]) -> None:
        self.__clear_contents()
        for content in contents:
            self.__browser.insert('', END, values=content)


