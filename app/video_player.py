import sys
import traceback
from tkinter import *
from tkinter import ttk

from .core.videos_db import VideosDB
from .core.video_library import LibraryItemCollection
from .core.search_engine import SearchEngine
from .widgets import MainLayout
from .namespace import Widgets

class MainFrame(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
         
        for column in range(3):
            self.columnconfigure(column, weight=1)

        self.__create_widgets()

    def __create_widgets(self):
        ttk.Label(
                self,
                text='Select an option by clicking one of the buttons below'
                ).grid(row=0, column=0, columnspan=3)
        ttk.Button(
                self,
                text='Check Videos',
                command=lambda: self._root().display_frame('check_videos')
                ).grid(row=1, column=0)
        ttk.Button(
                self,
                text='Create Video List',
                command=lambda: self._root().display_frame('create_video_list')
                ).grid(row=1, column=1)
        ttk.Button(
                self,
                text='Update Videos',
                command=lambda: self._root().display_frame('update_videos')
                ).grid(row=1, column=2)

        for widget in self.winfo_children():
            widget.grid(padx=5, pady=5, sticky=(W, E))

    def display(self):
        self.grid(row=0, column=0, sticky=NSEW)

class VideoPlayer(Tk):
    def __init__(self):
        super().__init__()

        self.__curr_frame = None
        self.__frames = {}
      
        MainLayout(self)
        self.title('Video Player')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.resizable(False, False)
        self.__create_widgets()
        self.display_frame('main')
    
    def display_frame(self, frame):
        try:
            frame, kwargs = self.__frames[frame]
            
        except KeyError as e:
            print(f'frame not found: {frame}', file=sys.stderr)
            traceback.print_stack(file=sys.stderr)
        else:
            if (self.__curr_frame is not None):
                self.__curr_frame.grid_forget()
            self.__curr_frame = frame
            self.__curr_frame.display(**kwargs)

    def __create_widgets(self):
        self.__frames['main'] = (MainFrame(self), {})
        self.__frames['check_videos'] = (Widgets.MAIN_LAYOUT, {'rpanel': Widgets.CHECK_VIDEOS_PANEL})
        self.__frames['update_videos'] = (Widgets.MAIN_LAYOUT, {'rpanel': Widgets.UPDATE_VIDEO_PANEL})
        self.__frames['create_video_list'] = (Widgets.MAIN_LAYOUT, {'rpanel': Widgets.CREATE_VIDEO_LIST_PANEL})
