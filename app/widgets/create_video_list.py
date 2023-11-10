from tkinter import *
from tkinter import ttk

from . import VideoFrame
from app.core.video_library import LibraryItemCollection
from ..events.event_handlers import EventHandler
from ..events.events import PlaylistButtonClickEvent 

class CreateVideoListFrame(VideoFrame):
    def __init__(self, root):
        self.__info_var = StringVar()
        self._curr_playlist = LibraryItemCollection()
        super().__init__(root)

    def _create_widgets(self):
        ttk.Label(
                self,
                text='Playlist'
            ).grid(column=1, row=0, sticky=S)
        ttk.Label(
                self,
                textvariable=self.__info_var
            ).grid(column=1, row=2, sticky=(W, S))
        ttk.Label(
                self,
                text='Enter movie number:'
            ).grid(column=1, row=3, sticky=(W, S))

        video_entry = ttk.Entry(
                self,
                textvariable=self._video_id,
                validate='key',
                validatecommand=self._number_input_validate
            )
        video_entry.grid(row=4, column=1, sticky=(N, W, E, S))
        video_entry.focus()

        self.__rm_pl_btn = ttk.Button(
                self,
                text='Remove from playlist'
            )
        self.__rm_pl_btn.grid(row=5, column=1, sticky=(N, W, E, S))
        self.__add_pl_btn = ttk.Button(
                self,
                text='Add to playlist'
            )       
        self.__add_pl_btn.grid(row=6, column=1, sticky=(N, W, E, S))
        self.__play_pl_btn = ttk.Button(
                self,
                text='Play the playlist'
            )
        self.__play_pl_btn.grid(row=8, column=1, sticky=(N, W, E, S))

    def _bind_events(self):
        event = PlaylistButtonClickEvent(self)
        self.__add_pl_btn.bind('<Button-1>', EventHandler.add_to_playlist(event))
        self.__rm_pl_btn.bind('<Button-1>', EventHandler.remove_from_playlist(event))
        self.__play_pl_btn.bind('<Button-1>', EventHandler.play_playlist(event))

    def _update_texts(self, status, text_info):
        self.__info_var.set(text_info)

        if not status: return

        playlist = '\n'.join(video.get_name() for video in self._curr_playlist)
        self._display_info(playlist)
