from tkinter import *
from tkinter import ttk

from video_frame import VideoFrame
from video_library import VideoCollection

class CreateVideoListFrame(VideoFrame):
    def __init__(self, root, db):
        super().__init__(root, db)
        self.__info_var = StringVar()
        self.__curr_playlist = VideoCollection()
        self._create_widgets()

    def _create_widgets(self):
        ttk.Label(
                self,
                text='Playlist'
                ).grid(column=1, row=0, sticky=S)
        ttk.Label(
                self,
                textvariable=self.__info_var
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
                width=20,
                command=self.__remove_from_playlist,
                ).grid(pady=3, row=5, column=1, sticky=(N, W, E, S))
        ttk.Button(
                self,
                text='Add to playlist',
                width=20,
                command=self.__add_to_playlist,
                ).grid(pady=3, row=6, column=1, sticky=(N, W, E, S))
        ttk.Button(
                self,
                text='Play the playlist',
                width=20,
                command=self.__play_playlist,
                ).grid(pady=5, row=8, column=1, sticky=(N, W, E, S))

        for widget in self.winfo_children():
           widget.grid(padx=5)

    def __update_texts(self, status, text_info):
        self.__info_var.set(text_info)

        if not status: return

        playlist = '\n'.join(video.name for video in self.__curr_playlist)
        self._display_info(playlist)
        
    def __add_to_playlist(self):
        id = self._video_id.get()
        status = True
        message = 'Added'
        try:
            video = self._db.get_video_by_id(id)
            self.__curr_playlist.add(video)
        except KeyError as e:
            message = f'Video id not found {id}'
            status = False
        finally:
            self.__update_texts(status, message)

    def __remove_from_playlist(self):
        id = self._video_id.get()
        status = True
        message = 'Removed!'
        try:
            self.__curr_playlist.remove(id)
        except KeyError as e:
            message = f'This video has not been added to playlist!'
            status = False
        finally:
            self.__update_texts(status, message)

    def __play_playlist(self):
        message = 'Played!'
        
        if not self.__curr_playlist:
            message = 'No video to play'
        
        for video in self.__curr_playlist:
            self._db.increment_play_count(video.id)

        self.__update_texts(True, message)
