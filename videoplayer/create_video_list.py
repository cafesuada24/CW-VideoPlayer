from tkinter import *
from tkinter import ttk

from video_frame import VideoFrame

class CreateVideoListFrame(VideoFrame):
    def __init__(self, root, db):
        super().__init__(root, db)
        self.__err_var = StringVar()
        self._create_widgets()

    def _create_widgets(self):
        ttk.Label(
                self,
                text='Playlist'
                ).grid(column=1, row=0, sticky=S)
        ttk.Label(
                self,
                textvariable=self.__err_var
                ).grid(pady=5, column=1, row=2, sticky=(W, S))
        ttk.Label(
                self,
                text='Enter movie number:'
                ).grid(pady=5, column=1, row=3, sticky=(W, S))

        video_entry = ttk.Entry(
                self,
                width=35,
                textvariable=self._video_id,
                validate='key',
                validatecommand=self._number_input_validate
                )
        video_entry.grid(row=4, column=1, sticky=(N, W, E, S))
        video_entry.focus()

        ttk.Button(
                self,
                text='Remove from playlist',
                width=20
                ).grid(pady=3, row=5, column=1, sticky=(N, W, E, S))
        ttk.Button(
                self,
                text='Add to playlist',
                width=20
                ).grid(pady=3, row=6, column=1, sticky=(N, W, E, S))
        ttk.Button(
                self,
                text='Play the playlist',
                width=20
                ).grid(pady=5, row=8, column=1, sticky=(N, W, E, S))

        for widget in self.winfo_children():
           widget.grid(padx=5)
