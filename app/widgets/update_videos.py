import tkinter as tk
from tkinter import ttk

from ..singleton import SingletonMeta
from ..namespaces.event_handlers import EventHandlers
from ..namespaces.tk_variable import TkVariable
from ..namespaces.general import General
from ..core.video_library import LibraryItem
from .abstracts import AppFrame


class UpdateVideoPanel(AppFrame, metaclass=SingletonMeta):
    def __init__(self, root):
        super().__init__(root)

        TkVariable().selected_id.trace_add('write', self.__display_info)

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=3)

    def _create_widgets(self):
        self.__attrs = LibraryItem.HEADINGS
        self.__vars = (TkVariable().selected_id,) + tuple(
            tk.StringVar() for _ in range(1, len(self.__attrs))
        )
        self.__entries = tuple(
            ttk.Entry(self, width=35, textvariable=var) for var in self.__vars
        )
        self.__update_btn = ttk.Button(
            self, text='Update', width=20, command=EventHandlers().update_video
        )

    def _display_widgets(self):
        ttk.Label(self, text='Update Video').grid(
            row=0, column=0, columnspan=2
        )
        for row in range(1, 14, 2):
            ttk.Separator(self, orient='horizontal').grid(
                row=row, column=0, columnspan=2, sticky='nsew'
            )

        for row, attr, entry in zip(
            range(2, 13, 2), self.__attrs, self.__entries
        ):
            ttk.Label(self, text=attr).grid(row=row, column=0, sticky='w')
            entry.grid(row=row, column=1, ipady=3, sticky='e')

        self.__update_btn.grid(row=15, column=1, sticky='e')

    def __display_info(self, *ignore):
        id = TkVariable().get_selected_id(display_msg=False)
        if not id:
            return
        data = General().data[id].list_all()[1:]
        for idx, value in enumerate(data, start=1):
            self.__vars[idx].set(value)
