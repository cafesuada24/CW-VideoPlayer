import sys
import traceback
from tkinter import *
from tkinter import ttk

from .widgets.check_videos import CheckVideosFrame
from .core.videos_db import VideosDB
from .core.video_library import LibraryItemCollection
from .core.search_engine import SearchEngine

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
                command=lambda: self._root()._display_frame('check_videos')
                ).grid(row=1, column=0)
        ttk.Button(
                self,
                text='Create Video List',
                command=lambda: self._root()._display_frame('create_video_list')
                ).grid(row=1, column=1)
        ttk.Button(
                self,
                text='Update Videos',
                command=lambda: self._root()._display_frame('update_videos')
                ).grid(row=1, column=2)

        for widget in self.winfo_children():
            widget.grid(padx=5, pady=5, sticky=(W, E))

class VideoPlayer(Tk):
    def __init__(self):
        super().__init__()
        # 
        self.__curr_frame = None
        self.__frames = {}
        # self.__db = VideosDB()
        # self.__videos = LibraryItemCollection.from_sequences(self.__db.get_all())
        # data = []
        # for video in self.__videos:
        #     video_info = video.list_all(('name', 'director'))
        #     video_info = (text.lower() for text in video_info)
        #     data.extend(zip(video_info, [video.id] * 2))
        # self.__se = SearchEngine(data)
        
        self.title('Video Player')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.resizable(width=False, height=False)
        self.__create_widgets()
        self._display_frame('main')
    
    @property
    def se(self):
        return self.__se

    @property
    def videos(self):
        return self.__videos
    
    @property
    def db(self):
        return self.__db
    
    def _display_frame(self, frame):
        try:
            frame = self.__frames[frame]
        except KeyError as e:
            print(f'frame not found: {frame}', file=sys.stderr)
            traceback.print_stack(file=sys.stderr)
        else:
            if (self.__curr_frame is not None):
                self.__curr_frame.grid_forget()
            self.__curr_frame = frame
            self.__curr_frame.grid(column=0, row=0, sticky=(N, S, E, W))

    def __create_widgets(self):
        self.__frames['main'] = MainFrame(self)
        self.__frames['check_videos'] = CheckVideosFrame(self)
        # self.__frames['update_videos'] = UpdateVideosFrame(self)
        # self.__frames['create_video_list'] = CreateVideoListFrame(self)
