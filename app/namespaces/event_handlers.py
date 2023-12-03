"""This module contains namespace of button event handlers"""

import tkinter as tk
from tkinter import messagebox as msgbox
from collections.abc import Sequence

from .tk_variable import TkVariable
from .general import General
from ..core.video_library import LibraryItem, LibraryItemCollection
from ..widgets.media_player import MediaPlayer


class EventHandlers:
    """Event handers namespace

    The purpose of @static is for readbility and namespace properties
    """

    @staticmethod
    def get_brower_items() -> None:
        """Returns filtered videos"""

        _prefix = TkVariable().get_search_entry()  # Search prefix
        _data = General().search_engine.search_prefix(
            _prefix
        )  # Filter by search_prefix
        _data = (General().data[id] for id in _data)  # Fetch data
        d = {
            'id': 'video_id',
            'author': 'director',
            'name': 'name',
            'rating': 'rating',
        }  # corresponded sort option
        sort_by = TkVariable().get_sort_by()  # get sort option
        sort_order = TkVariable().get_sort_order()  # get sort direction
        return sorted(
            _data, key=lambda val: val[d[sort_by]], reverse=sort_order
        )  # sort data by sort option and direction

    @staticmethod
    def play_video():
        """Plays the selected video"""

        video = EventHandlers.get_video()
        if not video:
            return
        playlist = LibraryItemCollection((video,))  # Create playlist
        MediaPlayer().play(playlist)

    @staticmethod
    def get_video() -> LibraryItem:
        """Returns current selected video"""

        id = TkVariable().get_selected_id()
        if not id:
            return None
        return General().data[id]

    @staticmethod
    def add_selected_to_playlist() -> bool:
        """Adds selected video to the current playlist
        Returns:
            a boolean of action status
        """

        video = EventHandlers.get_video()
        if not video:
            return False
        if video.get_id() in General().play_list:
            msgbox.showerror('Add error', 'This video has been added')
            return False
        General().play_list.add(video)
        return True

    @staticmethod
    def remove_selected_from_playlist() -> bool:
        """Remove current selected videos from the current playlist
        Returns:
            a boolean of action status
        """

        id = TkVariable().get_selected_id()
        if not id:
            return False
        if id not in General().play_list:
            # display error if the video is not in playlist
            msgbox.showerror('Remove error', 'This video is not in playlist!')
            return False
        General().play_list.remove(id)
        return True

    @staticmethod
    def play_playlist() -> bool:
        """Play the current playlist
        Returns:
            a boolean of action status
        """

        if not General().play_list:
            # Show error if the playlist is empty
            msgbox.showerror('Play error', 'Cannot play an empty playlist!')
            return False
        MediaPlayer().play(General().play_list)
        return True

    @staticmethod
    def update_video(columns, new_values: Sequence[tk.Entry]):
        """Update video informations
        Args:
            columns - column indexes to be updated
            new_values - tkiter variables corresponded to columns
        """

        video = EventHandlers.get_video()
        if not video:
            return
        try:
            # Try to fetch variables values
            new_values = tuple(item.get() for item in new_values)
        except tk._tkinter.TclError as e:
            msgbox.showinfo('Update error', e)
            return
        if all(val == video[index] for index, val in zip(columns, new_values)):
            # If there is no change
            msgbox.showinfo('Update', 'Nothing to update!')
            return
        if any(not val for val in new_values if isinstance(val, str)):
            # If there are invalid values
            msgbox.showerror('Update error', 'Entry cannot be empty!')
            return

        for col, new_val in zip(columns, new_values):
            if new_val != video[col]:
                # Update if new values if different
                video[col] = new_val
