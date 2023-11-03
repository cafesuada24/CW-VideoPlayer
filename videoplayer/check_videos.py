from tkinter import *
from tkinter import ttk

from video_frame import VideoFrame

class CheckVideosFrame(VideoFrame):
    def __init__(self, root):
        super().__init__(root)
        self.__video = StringVar()
        self._create_widgets()

    def _create_widgets(self):
        ttk.Label(
                self,
                text='Movie Information'
                ).grid(column=1, row=0, sticky=S)
        ttk.Label(
                self,
                text='Enter movie number or name:'
                ).grid(pady=5, column=1, row=6, sticky=(W, S))
       
        video_entry = ttk.Entry(self, width=35, textvariable=self.__video)
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
       self._insert_info(self.__video.get())
