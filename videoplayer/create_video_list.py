from tkinter import *
from tkinter import ttk

from video_frame import VideoFrame

class CreateVideoListFrame(VideoFrame):
    def __init__(self, root):
        super().__init__(root)
        
        self.__err_var = StringVar()
        self.__create_widgets()

    def __create_widgets(self):
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
                text='Enter movie number or name:'
                ).grid(pady=5, column=1, row=3, sticky=(W, S))

        entry = ttk.Entry(self, width=35)
        entry.grid(row=4, column=1, sticky=(N, W, E, S))
        entry.focus()

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
