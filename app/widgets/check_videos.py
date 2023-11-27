import tkinter as tk
from tkinter import ttk
from collections.abc import Sequence

from ..singleton import SingletonMeta
from ..namespaces.tk_variable import TkVariable
from ..namespaces.event_handlers import EventHandlers
from ..core.video_library import LibraryItem
from .abstracts import AppFrame, InfoText


class CheckVideosPanel(AppFrame, metaclass=SingletonMeta):
    COLUMNS = (1, 2, 3, 4, 5)
    HEADINGS = tuple(LibraryItem.HEADINGS[col] for col in COLUMNS)

    def __init__(self, root):
        super().__init__(root)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)

    def _create_widgets(self):
        self.__texts = tuple(InfoText(self) for _ in range(len(self.COLUMNS)))
        self.__id_input = ttk.Entry(
            self, textvariable=TkVariable().selected_id
        )
        self.__check_btn = ttk.Button(
            self, text='Check Videos', width=20, command=self.__display_info
        )
        self.__play_btn = ttk.Button(self, text='Play', width=20, command=EventHandlers().play_video)

    def _display_widgets(self):
        ttk.Label(self, text='Video Infomation').grid(
            row=0, column=0, columnspan=2, sticky='ns'
        )
        ttk.Label(self, text=LibraryItem.HEADINGS[0]).grid(
            row=2, column=0, sticky='w'
        )
        self.__id_input.grid(row=2, column=1, ipady=3, sticky='we')
        self.__play_btn.grid(row=14, column=0, columnspan=2, sticky='wns')
        self.__check_btn.grid(row=14, column=1, sticky='ens')

        for idx in range(0, 2 + len(self.COLUMNS)):
            row = 2 * idx + 1
            ttk.Separator(self, orient='horizontal').grid(
                row=row, column=0, columnspan=2, sticky='nsew'
            )

        for idx, (attr, text) in enumerate(zip(
            self.HEADINGS, self.__texts
        )):
            row = 2 * (idx + 2)
            ttk.Label(self, text=attr).grid(row=row, column=0, sticky='w')
            text.grid(row=row, column=1, ipady=3, sticky='we')

    def __display_info(self):
        data = EventHandlers.get_video()
        if not data:
            for text in self.__texts:
                text.display('')
            return

        for text, col in zip(self.__texts, self.COLUMNS):
            text.display(data[col])
