import tkinter as tk
from tkinter import ttk

from ..singleton import SingletonMeta
from ..namespaces.event_handlers import EventHandlers
from ..namespaces.tk_variable import TkVariable
from ..namespaces.general import General
from ..core.video_library import LibraryItem
from .abstracts import AppFrame


class UpdateVideoPanel(AppFrame, metaclass=SingletonMeta):
    COLUMNS = (1, 2, 3, 5)
    HEADINGS = tuple(LibraryItem.HEADINGS[col] for col in COLUMNS)

    def __init__(self, root):
        super().__init__(root)

        TkVariable().selected_id.trace_add('write', self.__display_info)

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=3)

    def _create_widgets(self):
        self.__vars = (
            tk.StringVar(),
            tk.StringVar(),
            tk.DoubleVar(),
            tk.StringVar(),
        )
        self.__id_input = ttk.Entry(
            self, width=35, textvariable=TkVariable().selected_id
        )
        self.__entries = tuple(
            ttk.Entry(self, width=35, textvariable=var) for var in self.__vars
        )
        self.__update_btn = ttk.Button(
            self,
            text='Update',
            width=20,
            command=lambda: EventHandlers().update_video(self.__vars),
        )

    def _display_widgets(self):
        ttk.Label(self, text='Update Video').grid(
            row=0, column=0, columnspan=2
        )
        ttk.Label(self, text='ID').grid(row=2, column=0, sticky='w')
        for idx in range(0, 2 + len(self.COLUMNS)):
            row = idx * 2 + 1
            ttk.Separator(self, orient='horizontal').grid(
                row=row, column=0, columnspan=2, sticky='nsew'
            )
        for idx, (attr, entry) in enumerate(
            zip(self.HEADINGS, self.__entries)
        ):
            row = 2 * (idx + 2)
            ttk.Label(self, text=attr).grid(row=row, column=0, sticky='w')
            entry.grid(row=row, column=1, ipady=3, sticky='e')

        self.__id_input.grid(row=2, column=1, ipady=3, sticky='e')
        self.__update_btn.grid(row=15, column=1, sticky='e')

    def __display_info(self, *ignore):
        id = TkVariable().get_selected_id(display_msg=False)
        if not id:
            for var in self.__vars:
                var.set('' if isinstance(var, tk.StringVar) else 0)
            return
        data = General().data[id]
        for idx, col in enumerate(self.COLUMNS):
            self.__vars[idx].set(data[col])
