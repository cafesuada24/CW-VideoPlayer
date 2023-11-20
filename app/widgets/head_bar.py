from tkinter import *
from tkinter import ttk

from ..namespace import Widgets, Variable, General

class HeadBar(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        
        self.__sort_by_var = StringVar()
        self.__sort_order_var = StringVar()
        self.__list_video_btn = ttk.Button(self, text='List All Videos', command=self.__update_brower_items)
        self.__sort_by = ttk.OptionMenu(self, self.__sort_by_var, 'ID    ', *('ID    ', 'Name  ', 'Author', 'Rating'), direction='below')
        self.__sort_order = ttk.OptionMenu(self, self.__sort_order_var, 'Ascending ', *('Ascending ', 'Descending'))
        self.__search_bar = Entry(self, textvariable=Variable.search_entry)
         
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
        _prefix = Variable.search_entry.get().strip().lower()
        _ids = General.search_engine.search_prefix(_prefix)
        _data = [General.data[id] for id in _ids] 
        d = {'id': 'video_id', 'author': 'director', 'name': 'name', 'rating': 'rating'}
        sort_by = self.__sort_by_var.get().strip().lower()
        sort_order = self.__sort_order_var.get().strip().lower()
        _data.sort(key=lambda val: val[d[sort_by]], reverse=sort_order=='descending')
        Widgets.BROWSER.display_items(_data)

        

