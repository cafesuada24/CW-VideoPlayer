import tkinter as tk
from tkinter import ttk

from ..singleton import SingletonMeta
from ..namespaces.event_handlers import EventHandlers
from ..namespaces.tk_variable import TkVariable
from ..core.video_library import LibraryItem
from ..core.videos_db import VideosDB
from .abstracts import AppFrame


class VideoBrowser(AppFrame, metaclass=SingletonMeta):
    COLUMNS = (0, 1, 2, 3)

    def __init__(self, root):
        super().__init__(root)

        for children in self.winfo_children():
            children.grid(padx=0)

    def _create_widgets(self):
        columns_width = (50, 300, 300, 150)
        self.__browser = ttk.Treeview(self, show='headings', height=20)
        self.__scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.__browser.yview)
        self.__browser['yscrollcommand'] = self.__scrollbar.set
        self.__browser['columns'] = tuple(
            VideosDB.COLUMNS[column] for column in self.COLUMNS
        )
        for column in self.COLUMNS:
            self.__browser.heading(
                VideosDB.COLUMNS[column], text=LibraryItem.HEADINGS[column]
            )
            self.__browser.column(
                VideosDB.COLUMNS[column], width=columns_width[column]
            )

        self.__browser.bind('<<TreeviewSelect>>', self.__item_selected)

    def _display_widgets(self):
        self.__browser.grid(row=0, column=0, sticky='nsew')
        self.__scrollbar.grid(row=0, column=1, sticky='nsew')

    def __clear_contents(self):
        for item in self.__browser.get_children():
            self.__browser.delete(item)
    
    def __item_selected(self, *ignore):
        selected = self.__browser.selection()
        if not selected:
            return
        id = TkVariable().get_selected_id(display_msg=False)
        if id != selected[0]:
            TkVariable().selected_id.set(selected[0])

    def display_playlist(self) -> None:
        contents = EventHandlers.get_brower_items()
        if not contents:
            return
        self.__clear_contents()
        for item in contents:
            self.__browser.insert(
                '', tk.END, id=item.get_id(), values=item.list_all(self.COLUMNS)
            )
        
        first_element = int(self.__browser.get_children()[0])
        self.__browser.selection_set(first_element)
