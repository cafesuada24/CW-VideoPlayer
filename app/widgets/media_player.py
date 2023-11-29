import tkinter as tk
from tkinter import ttk
from pathlib import Path

from tkvideo import tkvideo

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
        self.__media_player = ttk.Label(self)
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
        player = tkvideo(playlist[0].get_file_path(), self.__media_player, loop=1, size=(1280, 720))
        player.play()
        self.mainloop()
        self.__playing = False

