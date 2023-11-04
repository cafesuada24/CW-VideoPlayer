from tkinter import *
from tkinter import ttk

from video_frame import VideoFrame

class CheckVideosFrame(VideoFrame):
    def __init__(self, root, db):
        super().__init__(root, db)
        self.__movie_infors = ('Name', 'Director', 'Rating', 'Play count')
        self._create_widgets()

    def _create_widgets(self):
        ttk.Label(
                self,
                text='Movie Information'
                ).grid(column=1, row=0, sticky=S)
        ttk.Label(
                self,
                text='Enter movie number:'
                ).grid(pady=5, column=1, row=6, sticky=(W, S))
       
        video_entry = ttk.Entry(
                self,
                width=35,
                textvariable=self._video_id,
                validate='key',
                validatecommand=self._number_input_validate
                )
        video_entry.grid(row=7, column=1, sticky=(N, W, E, S))
        video_entry.focus()
        
        ttk.Button(
                self,
                text='Check Video',
                width=20,
                command=self.__check_video,
                ).grid(pady=5, row=8, column=1, sticky=(N, W, E, S))

        for widget in self.winfo_children():
           widget.grid(padx=5)
    
    def __check_video(self):
        id = self._video_id.get()
        try:
            video_attr = (self._db.get_name(id), self._db.get_director(id), self._db.get_rating(id), self._db.get_play_count(id))
            video_attr = (f'{attr}: {val}' for attr, val in zip(self.__movie_infors, video_attr))
            self._display_info('\n'.join(video_attr))
        except KeyError as e:
            self._display_info(f'Video id not found: {id}')
