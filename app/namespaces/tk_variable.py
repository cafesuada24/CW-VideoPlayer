import tkinter as tk
from ..singleton import SingletonMeta
from .general import General


class TkVariable(metaclass=SingletonMeta):
    def __init__(self):
        self.__selected_id = tk.IntVar()
        self.__search_entry = tk.StringVar()
        self.__sort_by = tk.StringVar()
        self.__sort_order = tk.StringVar()

    def get_selected_id(self, display_msg=True):
        try:
            id = self.selected_id.get()
            if id not in General().data:
                raise KeyError('Invalid ID')
        except Exception as e:
            if not display_msg:
                return
            tk.messagebox.showerror('Id error', message='Invalid ID')
        else:
            return id

    def get_search_entry(self):
        return self.__search_entry.get().strip().lower()

    def get_sort_by(self):
        return self.__sort_by.get().strip().lower()

    def get_sort_order(self):
        return self.__sort_order.get().strip().lower() == 'descending'

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
