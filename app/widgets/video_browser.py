import tkinter as tk
from tkinter import ttk
from collections.abc import Sequence

from ..singleton import SingletonMeta
from ..namespaces.event_handlers import EventHandlers
from ..namespaces.tk_variable import TkVariable
from ..core.video_library import LibraryItem


class VideoBrowser(ttk.Frame, metaclass=SingletonMeta):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__columns = (0, 1, 2, 3)
        columns_width = (50, 300, 300, 150)
        self.__browser = ttk.Treeview(self, show='headings', height=20)
        self.__browser['columns'] = tuple(
            LibraryItem.COLUMNS[column] for column in self.__columns
        )
        for column in self.__columns:
            self.__browser.heading(
                LibraryItem.COLUMNS[column], text=LibraryItem.HEADINGS[column]
            )
            self.__browser.column(
                LibraryItem.COLUMNS[column], width=columns_width[column]
            )

        self.__browser.bind('<<TreeviewSelect>>', self.__item_selected)
        self.__browser.grid(row=0, column=0, sticky='nsew')

    def __clear_contents(self):
        for item in self.__browser.get_children():
            self.__browser.delete(item)

    def __item_selected(self, *ignore):
        selected = self.__browser.focus()
        selected = self.__browser.item(selected)['values']
        if not len(selected):
            return
        TkVariable().selected_id.set(selected[0])

    def display_playlist(self) -> None:
        contents = EventHandlers.get_brower_items()
        if not contents:
            return
        self.__clear_contents()
        for content in contents:
            self.__browser.insert(
                '', tk.END, values=content.list_all(self.__columns)
            )
