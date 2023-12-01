"""This module contains namespace of all general Tkinter Variable"""

import tkinter as tk
from ..singleton import SingletonMeta
from .general import General


class TkVariable(metaclass=SingletonMeta):
    """Namespace contains variable, and method to access its values

    The purpose of @porperty is for readability and preventing changes
    """

    def __init__(self):
        self.__selected_id = tk.IntVar()  # value of all id entries
        self.__search_entry = tk.StringVar()  # value of search bar
        self.__sort_by = tk.StringVar()  # value of sorting selection
        self.__sort_order = tk.StringVar()  # value of sort order

    def get_selected_id(self, display_msg=True):
        """Get the current selected id
        Args:
            display_msg - a boolean to decide if a messagebox is display when the id is invalid

        Returns:
            id - integer selected id
        or
            none if id is invalid
        """

        try:
            id = self.selected_id.get()  # get value of tkvar
            if id not in General().data:  # check validity
                raise KeyError('Invalid ID')
        except Exception as e:
            if not display_msg:
                return
            tk.messagebox.showerror('Id error', message='Invalid ID')
        else:
            return id

    def get_search_entry(self):
        """Returns search value"""
        return self.__search_entry.get().strip().lower()

    def get_sort_by(self):
        """Returns sort option"""

        return self.__sort_by.get().strip().lower()

    def get_sort_order(self):
        """Returns sort order"""

        return self.__sort_order.get().strip().lower() == 'descending'

    @property
    def selected_id(self):
        """Return the selected_id variable"""

        return self.__selected_id

    @property
    def search_entry(self):
        """Return the search_entry variable"""

        return self.__search_entry

    @property
    def sort_by(self):
        """Returns the sort_by variable"""

        return self.__sort_by

    @property
    def sort_order(self):
        """Returns the sort_order variable"""

        return self.__sort_order
