import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbox

from ..singleton import SingletonMeta
from ..core.video_library import LibraryItemCollection, LibraryItem
from ..namespaces.event_handlers import EventHandlers
from ..namespaces.tk_variable import TkVariable
from ..namespaces.general import General
from .abstracts import AppFrame, InfoText


class CreateVideoListPanel(AppFrame, metaclass=SingletonMeta):
    def __init__(self, root):
        super().__init__(root)

        TkVariable().selected_id.trace_add('write', self.__display_name)

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=3)

    def _create_widgets(self):
        self.__attrs = LibraryItem.HEADINGS[1:2]
        self.__playlist = tk.Listbox(self, width=50)
        self.__id_entry = ttk.Entry(
            self, textvariable=TkVariable().selected_id
        )
        self.__texts = tuple(InfoText(self) for _ in range(len(self.__attrs)))
        self.__add_btn = ttk.Button(
            self,
            text='Add',
            width=20,
            command=self.display_playlist(
                EventHandlers().add_selected_to_playlist
            ),
        )
        self.__remove_btn = ttk.Button(
            self,
            text='Remove',
            width=20,
            command=self.display_playlist(
                EventHandlers().remove_selected_from_playlist
            ),
        )
        self.__play_btn = ttk.Button(
            self,
            text='Play playlist',
            command=self.display_playlist(EventHandlers().play_playlist),
        )

    def _display_widgets(self):
        ttk.Label(self, text='Create video list').grid(
            row=0, column=0, columnspan=2
        )
        ttk.Label(self, text='ID').grid(row=4, column=0, sticky='w')
        for row in range(1, 8, 2):
            ttk.Separator(self, orient='horizontal').grid(
                row=row, column=0, columnspan=2, sticky='nsew'
            )
        self.__playlist.grid(row=2, column=0, columnspan=2)
        self.__id_entry.grid(row=4, column=1, ipady=3, sticky='nsew')

        for row, attr, text in zip(range(6, 7, 2), self.__attrs, self.__texts):
            ttk.Label(self, text=attr).grid(row=row, column=0, sticky='w')
            text.grid(row=row, column=1, ipady=3, sticky='nsew')

        self.__add_btn.grid(column=0, row=8, columnspan=2, sticky='w')
        self.__remove_btn.grid(column=1, row=8, sticky='e')
        self.__play_btn.grid(column=0, columnspan=2, sticky='we')

    def __display_name(self, *ignore):
        id = TkVariable().get_selected_id(display_msg=False)
        if not id:
            return
        for text, value in zip(
            self.__texts, General().data[id].list_all(('name',))
        ):
            text.display(value)

    def display_playlist(self, call_back):
        def __wrapper():
            succ = call_back()
            if not succ:
                return
            self.__playlist.delete(0, tk.END)
            self.__playlist.insert(
                tk.END,
                *(
                    f'{item.get_id()} - {item.get_name()}'
                    for item in General().play_list
                ),
            )

        return __wrapper
