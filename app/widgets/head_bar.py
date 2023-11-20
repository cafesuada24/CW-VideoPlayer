from tkinter import *
from tkinter import ttk

from .search_bar import SearchBar
from ..namespace import DB, Widgets

class HeadBar(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        
        self.__state = DB.data.values()
        self.__sort_by_var = StringVar()
        self.__sort_order_var = StringVar()
        self.__list_video_btn = ttk.Button(self, text='List All Videos', command=self.__update_brower_items)
        self.__sort_by = ttk.OptionMenu(self, self.__sort_by_var, 'Number', *('Number', 'Name  ', 'Author', 'Rating'), direction='below')
        self.__sort_order = ttk.OptionMenu(self, self.__sort_order_var, 'Ascending ', *('Ascending ', 'Descending'))
        self.__search_bar = SearchBar(self)
         
        for col in range(6):
            self.columnconfigure(col, weight=1)
        self.columnconfigure(6, weight=2, minsize=200)

        Label(self, text='Sort by ').grid(row=0, column=1, sticky=E)
        Label(self, text='Sort order ').grid(row=0, column=3, sticky=E)
        Label(self, text='Search ').grid(row=0, column=5, sticky=E)

        self.__list_video_btn.grid(row=0, column=0, sticky=W)
        self.__sort_by.grid(row=0, column=2, sticky=W)
        self.__sort_order.grid(row=0, column=4, sticky=W)
        self.__search_bar.grid(row=0, column=6, sticky=(W, E))
    
    def __update_brower_items(self):
        sort_by = self.__sort_by_var.get().strip().lower()
        sort(self.__state, key=lambda val: val[sort_by], reverse=self.__sort_order_var=='Ascending')
        Widgets.BROWSER.display_items(self.__state)

        

