"""This module contains class for Create Video List window"""

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
    COLUMNS = (1,)  # database column indexes
    HEADINGS = tuple(
        LibraryItem.HEADINGS[col] for col in COLUMNS
    )  # get corresponded column headings

    def __init__(self, root):
        super().__init__(root)

        # Name field will be updated when selected_id changes
        TkVariable().selected_id.trace_add('write', self.__display_name)

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=3)

    def _create_widgets(self):
        self.__playlist_fr = ttk.Frame(self)  # Frame for playlist listbox
        self.__playlist = tk.Listbox(
            self.__playlist_fr, width=45
        )  # Listbox contains added videos
        self.__sb = ttk.Scrollbar(
            self.__playlist_fr, orient='vertical'
        )  # playlist listbox
        self.__id_entry = ttk.Entry(
            self, textvariable=TkVariable().selected_id
        )  # Selected video_id entry
        self.__texts = tuple(
            InfoText(self) for _ in range(len(self.HEADINGS))
        )  # All information text field
        self.__add_btn = ttk.Button(
            self,
            text='Add',
            width=20,
            command=self.display_playlist(
                EventHandlers().add_selected_to_playlist
            ),
        )  # Video will be added to be playlist when clicked
        self.__remove_btn = ttk.Button(
            self,
            text='Remove',
            width=20,
            command=self.display_playlist(
                EventHandlers().remove_selected_from_playlist
            ),
        )  # Video will be removed from playlist when clicked
        self.__play_btn = ttk.Button(
            self,
            text='Play playlist',
            command=self.display_playlist(EventHandlers().play_playlist),
        )  # Playlist will be played when clicked

        self.__playlist.config(yscrollcommand=self.__sb.set)  # Set Scrollbar
        self.__sb.config(command=self.__playlist.yview)  #

    def _display_widgets(self):
        ttk.Label(self, text='Create video list').grid(
            row=0, column=0, columnspan=2
        )
        ttk.Label(self, text='ID').grid(row=4, column=0, sticky='w')
        for idx in range(0, 3 + len(self.COLUMNS)):
            row = 2 * idx + 1
            ttk.Separator(self, orient='horizontal').grid(
                row=row, column=0, columnspan=2, sticky='nsew'
            )
        self.__playlist_fr.grid(row=2, column=0, columnspan=2)
        self.__id_entry.grid(row=4, column=1, ipady=3, sticky='nsew')

        for idx, (attr, text) in enumerate(zip(self.HEADINGS, self.__texts)):
            # Display all field and corresponded heading
            row = 2 * (idx + 3)
            ttk.Label(self, text=attr).grid(row=row, column=0, sticky='w')
            text.grid(row=row, column=1, ipady=3, sticky='nsew')

        self.__add_btn.grid(column=0, row=8, columnspan=2, sticky='w')
        self.__remove_btn.grid(column=1, row=8, sticky='e')
        self.__play_btn.grid(column=0, columnspan=2, sticky='we')
        self.__playlist.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.__sb.pack(side=tk.RIGHT, fill=tk.Y)

    def __display_name(self, *ignore):
        """Display video name"""

        id = TkVariable().get_selected_id(display_msg=False)
        if not id:
            # Clear all field and exit if id is invalid
            for text in self.__texts:
                text.display('')
            return
        data = General().data[id]
        for idx, col in enumerate(self.COLUMNS):
            # Display video's information
            self.__texts[idx].display(data[col])

    def display_playlist(self, call_back):
        """Wrappers for class event handlers

        Args:
            call_back: callable - event handler
        Return:
            decorated function
        """

        def __wrapper():
            succ = call_back()  # Action status
            if not succ:
                # If the action failed, return
                return

            # Update playlist if the action (add, remove, play) success
            self.__playlist.delete(0, tk.END)
            self.__playlist.insert(
                tk.END,
                *(
                    f'{item.get_id()} - {item.get_name()}'
                    for item in General().play_list
                ),
            )

        return __wrapper
