"""This module contains widgets of Update Video window"""

import tkinter as tk
from tkinter import ttk

from ..singleton import SingletonMeta
from ..namespaces.event_handlers import EventHandlers
from ..namespaces.tk_variable import TkVariable
from ..namespaces.general import General
from ..core.video_library import LibraryItem
from .abstracts import AppFrame


class UpdateVideoPanel(AppFrame, metaclass=SingletonMeta):
    COLUMNS = (1, 2, 3, 5)  # database column indexes
    HEADINGS = tuple(
        LibraryItem.HEADINGS[col] for col in COLUMNS
    )  # get corresponded column heading

    def __init__(self, root):
        super().__init__(root)

        # Attach new event, called when new video_id is selected
        TkVariable().selected_id.trace_add('write', self.__display_info)

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=3)

    def _create_widgets(self):
        self.__vars = (
            tk.StringVar(),
            tk.StringVar(),
            tk.DoubleVar(),
            tk.StringVar(),
        )  # corresponded variable for updating entries
        self.__id_input = ttk.Entry(
            self, width=35, textvariable=TkVariable().selected_id
        )  # video_id input
        self.__entries = tuple(
            ttk.Entry(self, width=35, textvariable=var) for var in self.__vars
        )  # Updating entries
        self.__update_btn = ttk.Button(
            self,
            text='Update',
            width=20,
            command=lambda: EventHandlers().update_video(
                self.COLUMNS, self.__vars
            ),
        )  # Update video information when clicked

    def _display_widgets(self):
        ttk.Label(self, text='Update Video').grid(
            row=0, column=0, columnspan=2
        )
        ttk.Label(self, text='ID').grid(row=2, column=0, sticky='w')
        for idx in range(0, 2 + len(self.COLUMNS)):
            # Display all separators
            row = idx * 2 + 1
            ttk.Separator(self, orient='horizontal').grid(
                row=row, column=0, columnspan=2, sticky='nsew'
            )
        for idx, (attr, entry) in enumerate(
            zip(self.HEADINGS, self.__entries)
        ):
            # Display all updating entries
            row = 2 * (idx + 2)
            ttk.Label(self, text=attr).grid(row=row, column=0, sticky='w')
            entry.grid(row=row, column=1, ipady=3, sticky='e')

        self.__id_input.grid(row=2, column=1, ipady=3, sticky='e')
        self.__update_btn.grid(row=15, column=1, sticky='e')

    def __display_info(self, *ignore):
        """Display video information"""

        id = TkVariable().get_selected_id(display_msg=False)
        if not id:
            # If id is invalid, reset entries and exit
            for var in self.__vars:
                var.set('' if isinstance(var, tk.StringVar) else 0)
            return
        data = General().data[id]
        for idx, col in enumerate(self.COLUMNS):
            self.__vars[idx].set(data[col])
