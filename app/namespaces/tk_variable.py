import tkinter as tk
from ..singleton import SingletonMeta

class TkVariable(metaclass=SingletonMeta):
    def __init__(self):
        self.__selected_id = tk.IntVar()
        self.__search_entry = tk.StringVar()
        self.__sort_by = tk.StringVar()
        self.__sort_order = tk.StringVar()

    @property
    def get_selected_id(self):
        try:
            id = self.selected_id.get()
        except Exception as e:
            print(e)
            msgbox.showerror('Id error', message='Invalid ID')
        return id
    
    @property
    def get_search_entry(self):
        return self.__search_entry.get()

    @property
    def get_sort_by(self):
        return self.__sort_by.get().strip().lower() == 'descending'

    @property
    def get_sort_order(self):
        return self.__sort_order.get().strip().lower()

    @property
    def selected_id(self):
        return self.__selected_id

    @property
    def search_entry(self):
        return self.__search_entry

    @property
    def sort_by(self):
        return self.__sort_by
    @property
    def sort_order(self):
        return self.__sort_order
