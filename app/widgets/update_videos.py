from tkinter import *
from tkinter import ttk

from . import VideoFrame
from ..events.events import UpdateButtonClickEvent 
from ..events.event_handlers import EventHandler

class UpdateVideosFrame(VideoFrame):
    def __init__(self, root):
        self._new_val = StringVar()
        self._update_column = StringVar()
        super().__init__(root)
        
    def _create_widgets(self):
        ttk.Label(self, text='Status').grid(column=2, row=0, sticky=S)
        ttk.Label(
            self,
            text='Enter movie number:'
        ).grid(column=2, row=2, sticky=(W, S))
        ttk.Label(
            self,
            text='Select attribute:'
        ).grid(column=2, row=4, sticky=(W, S))
        ttk.Label(self, text='Enter new value:').grid(
            column=2, row=6, sticky=(W, S)
        )

        ttk.Entry(
            self,
            textvariable=self._video_id,
            validate='key',
            validatecommand=self._number_input_validate
        ).grid(row=3, column=2, sticky=(N, W, E, S))

        combobox = ttk.Combobox(self, textvariable=self._update_column)
        combobox['state'] = 'readonly'
        combobox['values'] = ('rating', 'director', 'name')
        combobox.set('rating') 
        combobox.grid(column=2, row=5, sticky=(W, E, N))
        
        ttk.Entry(
            self,
            textvariable=self._new_val
        ).grid(row=7, column=2, sticky=(N, W, E, S))

        self.__update_btn = ttk.Button(
            self,
            text='Update',
            width=20
        ) 
        self.__update_btn.grid(row=8, column=2, sticky=(N, W, E, S))
    
    def _bind_events(self):
       self.__update_btn.bind(
           '<Button-1>',
           EventHandler.update_video(UpdateButtonClickEvent(self))
        ) 

