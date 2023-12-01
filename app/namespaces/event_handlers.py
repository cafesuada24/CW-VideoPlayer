# from .widgets import Widgets
import tkinter as tk
from tkinter import messagebox as msgbox
from collections.abc import Sequence

from .tk_variable import TkVariable
from .general import General
from ..core.video_library import LibraryItem, LibraryItemCollection
from ..widgets.media_player import MediaPlayer


class EventHandlers:
    @staticmethod
    def get_brower_items() -> None:
        _prefix = TkVariable().get_search_entry()
        _data = General().search_engine.search_prefix(_prefix)
        _data = (General().data[id] for id in _data)
        d = {
            'id': 'video_id',
            'author': 'director',
            'name': 'name',
            'rating': 'rating',
        }
        sort_by = TkVariable().get_sort_by()
        sort_order = TkVariable().get_sort_order()
        return sorted(
            _data, key=lambda val: val[d[sort_by]], reverse=sort_order
        )

    @staticmethod
    def play_video():
        video = EventHandlers.get_video()
        if not video:
            return
        playlist = LibraryItemCollection((video,))
        MediaPlayer().play(playlist)

    @staticmethod
    def get_video() -> LibraryItem:
        id = TkVariable().get_selected_id()
        if not id:
            return None
        return General().data[id]

    @staticmethod
    def add_selected_to_playlist() -> bool:
        video = EventHandlers.get_video()
        General().play_list.add(video)
        return True

    @staticmethod
    def remove_selected_from_playlist() -> bool:
        id = TkVariable().get_selected_id()
        if not id:
            return False
        if id not in General().play_list:
            msgbox.showerror(
                'Remove error', 'Seleted item is not in playlist!'
            )
            return False
        General().play_list.remove(id)
        return True

    @staticmethod
    def play_playlist() -> bool:
        if not General().play_list:
            msgbox.showerror('Play error', 'Cannot play an empty playlist!')
            return False
        MediaPlayer().play(General().play_list)
        return True

    @staticmethod
    def update_video(columns, new_values: Sequence[tk.Entry]):
        video = EventHandlers.get_video()
        if not video:
            return
        try:
            new_values = tuple(item.get() for item in new_values)
        except tk._tkinter.TclError as e:
            msgbox.showinfo('Update error', e)
            return
        if all(val == video[index] for index, val in zip(columns, new_values)):
            msgbox.showinfo('Update', 'Nothing to update!')
            return
        if any(not val for val in new_values if isinstance(val, str)):
            msgbox.showerror('Update error', 'Entry cannot be empty!')
            return

        for col, new_val in zip(columns, new_values):
            if new_val != video[col]:
                video[col] = new_val
