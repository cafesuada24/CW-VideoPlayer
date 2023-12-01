"""This module contains Video Browser class"""

import tkinter as tk
from tkinter import ttk

from ..singleton import SingletonMeta
from ..namespaces.event_handlers import EventHandlers
from ..namespaces.tk_variable import TkVariable
from ..core.video_library import LibraryItem
from ..core.videos_db import VideosDB
from .abstracts import AppFrame


class VideoBrowser(AppFrame, metaclass=SingletonMeta):
    COLUMNS = (0, 1, 2, 3)  # database column indexes

    def __init__(self, root):
        super().__init__(root)

        for children in self.winfo_children():
            children.grid(padx=0)

    def _create_widgets(self):
        columns_width = (50, 300, 300, 150)
        self.__browser = ttk.Treeview(
            self, show='headings', height=20
        )  # ALl videos will be displayed here
        self.__scrollbar = ttk.Scrollbar(
            self, orient='vertical', command=self.__browser.yview
        )  # Video Browser's scrollbar
        self.__browser.config(yscrollcommand=self.__scrollbar.set)
        self.__browser['columns'] = tuple(
            VideosDB.COLUMNS[column] for column in self.COLUMNS
        )  # Set browser columns
        for column in self.COLUMNS:
            # Config browser
            self.__browser.heading(
                VideosDB.COLUMNS[column], text=LibraryItem.HEADINGS[column]
            )
            self.__browser.column(
                VideosDB.COLUMNS[column], width=columns_width[column]
            )
        # called when an item in VideoBrowser is selected
        self.__browser.bind('<<TreeviewSelect>>', self.__item_selected)

    def _display_widgets(self):
        self.__browser.grid(row=0, column=0, sticky='nsew')
        self.__scrollbar.grid(row=0, column=1, sticky='nsew')

    def __clear_contents(self):
        """Clear video browser contents"""

        for item in self.__browser.get_children():
            self.__browser.delete(item)

    def __item_selected(self, *ignore):
        """Update id input when a video is selected"""

        selected = self.__browser.selection()  # get current selected item
        if not selected:
            return
        id = TkVariable().get_selected_id(display_msg=False)
        if id != selected[0]:
            TkVariable().selected_id.set(selected[0])

    def display_playlist(self) -> None:
        contents = EventHandlers.get_brower_items()  # Get all filtered videos
        if not contents:
            return
        # display contents
        self.__clear_contents()
        for item in contents:
            self.__browser.insert(
                '',
                tk.END,
                id=item.get_id(),
                values=item.list_all(self.COLUMNS),
            )

        # focus the first video in video browser
        id = TkVariable().get_selected_id(display_msg=False)
        if not id:
            id = int(self.__browser.get_children()[0])
        if self.__browser.exists(id):
            self.__browser.selection_set(id)
