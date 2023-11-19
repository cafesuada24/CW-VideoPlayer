from tkinter import *
from tkinter import ttk

from . import MainLayout
from .. import CONFIG
from ..events.event_handlers import EventHandler
from ..events.events import CheckButtonClickEvent


CONFIG = CONFIG['display']['columns']

class CheckVideosFrame(MainLayout):
    def __init__(self, root):
        super().__init__(root, rpanel=CheckVideosPanel)

    def _create_widgets(self):
        ttk.Label(
                self,
                text='Movie Information'
            ).grid(column=2, row=0, sticky=S)
        ttk.Label(
                self,
                text='Enter video number:'
            ).grid(column=2, row=6, sticky=(W, S))
       
        video_entry = ttk.Entry(
                self,
                textvariable=self._video_id,
                validate='key',
                validatecommand=self._number_input_validate
            )
        video_entry.grid(row=7, column=2, sticky=(N, W, E, S))
        video_entry.focus()
        
        self.__check_btn = ttk.Button(
                self,
                text='Check Video',
                width=20,
            )
        self.__check_btn.grid(row=8, column=2, sticky=(N, W, E, S))

    def _bind_events(self):
        self.__check_btn.bind(
            '<Button-1>',
            EventHandler.check_video(CheckButtonClickEvent(self))
        )

class CheckVideosPanel(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self['width'] = 50
