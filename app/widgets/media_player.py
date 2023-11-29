import tkinter as tk
from tkinter import ttk
from pathlib import Path

from tkVideoPlayer import TkinterVideo

from ..singleton import SingletonMeta
from .abstracts import AppFrame


class MediaPlayer(tk.Tk, metaclass=SingletonMeta):
    playing = False

    def __init__(self):
        super().__init__()
        self._create_widgets()
        self._display_widgets()
        
        self.__playing = False

        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=1)

    def _create_widgets(self):
        self.__media_player = TkinterVideo(self, scaled=True)
        self.__playlist_box = tk.Listbox(self)

    def _display_widgets(self):
        self.__media_player.grid(row=0, column=0, sticky='nsew')
        self.__playlist_box.grid(row=0, column=1, sticky='nsew')
        
    def play(self, play_list):
        if self.__playing:
            print('playing')
            return
        self.__playing = True
        playlist = tuple(play_list.values())
        self.__media_player.load(playlist[0].get_file_path())
        self.__media_player.play()
        self.mainloop()
        self.__playing = False

