"""This module contains root of all widgets in the application"""

import sys
import traceback
import tkinter as tk
from tkinter import ttk

from .core.videos_db import VideosDB
from .core.video_library import LibraryItemCollection
from .widgets.app_layout import MainLayout
from .widgets.video_browser import VideoBrowser
from .widgets.footer import Footer
from .widgets.head_bar import HeadBar
from .widgets.check_videos import CheckVideosPanel
from .widgets.create_video_list import CreateVideoListPanel
from .widgets.update_videos import UpdateVideoPanel
from .widgets.menu import Menu
from .widgets.media_player import MediaPlayer


class VideoPlayer(tk.Tk):
    """Root class"""

    def __init__(self):
        super().__init__()

        self.__curr_frame = None  # current displaying frame
        self.__frames = {}  # frames call information

        self.title('Video Player')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.resizable(False, False)
        self.__create_widgets()
        self.display_frame('menu')  # display the start menu

    def display_frame(self, frame):
        """Change to the specific frame
        Args:
            frame - name of the frame to switch
        """
        try:
            frame, kwargs = self.__frames[frame]

        except KeyError as e:
            print(f'frame not found: {frame}', file=sys.stderr)
            traceback.print_stack(file=sys.stderr)
        else:
            if self.__curr_frame is not None:
                self.__curr_frame.grid_forget()  # Hide current frame
            self.__curr_frame = frame
            self.__curr_frame.display(**kwargs)

    def __create_widgets(self):
        # Create all singleton widgets
        self.__main_layout = MainLayout(self)
        MediaPlayer(self)
        Menu(self)
        VideoBrowser(self.__main_layout)
        HeadBar(self.__main_layout)
        Footer(self.__main_layout)
        CheckVideosPanel(self.__main_layout)
        UpdateVideoPanel(self.__main_layout)
        CreateVideoListPanel(self.__main_layout)

        # Store all frame invoking information
        self.__frames['menu'] = (Menu(), {})
        self.__frames['check_videos'] = (
            self.__main_layout,
            {'rpanel': CheckVideosPanel()},
        )
        self.__frames['update_videos'] = (
            self.__main_layout,
            {'rpanel': UpdateVideoPanel()},
        )
        self.__frames['create_video_list'] = (
            self.__main_layout,
            {'rpanel': CreateVideoListPanel()},
        )
