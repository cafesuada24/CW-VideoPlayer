"""This module contains Top-Level window that plays the videos"""

import tkinter as tk
from tkinter import messagebox as msgbox
from tkinter import ttk
from pathlib import Path
import datetime

from tkVideoPlayer import TkinterVideo

from ..singleton import SingletonMeta
from ..core.videos_db import VideosDB
from ..core.video_library import LibraryItem


class MediaPlayer(tk.Toplevel, metaclass=SingletonMeta):
    """Top level window for playing a playlist"""

    COLUMNS = (0, 1)  # database columns indexes
    COLUMNS_WIDTH = (25, 150)

    def __init__(self, root):
        super().__init__(root)
        self.title('Play videos')
        self.minsize(width=960, height=540)

        self.protocol(
            'WM_DELETE_WINDOW', self.__on_close
        )  # Redefine close button 'x'
        self.__playlist = None  # Current play list
        self.__progress_value = tk.DoubleVar(self)  # Variable of progress bar

        self.rowconfigure(0, weight=6)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=2)

        self._create_widgets()
        self._display_widgets()

        self.withdraw()  # Hide the window

    def _create_widgets(self):
        self.__player = None  # Media player
        self.__start_label = ttk.Label(
            self, text=self.__time_to_str()
        )  # Video duration start
        self.__end_label = ttk.Label(
            self, text=self.__time_to_str()
        )  # Video duration end
        self.__play_btn = ttk.Button(
            self, text='Play', width=20, command=self.__play_pause
        )  # Play the video when clicked
        self.__select_video_btn = ttk.Button(
            self, text='Select video', width=20, command=self.__play_video
        )  # Load the selected video when clicked
        self.__progress_slider = ttk.Scale(
            self,
            from_=0,
            to=0,
            orient='horizontal',
            variable=self.__progress_value,
            command=self.__seek,
        )  # Time frame slider
        self.__video_browser = ttk.Treeview(
            self, height=20, show='headings'
        )  # Current playlist
        self.__video_browser['columns'] = tuple(
            VideosDB.COLUMNS[column] for column in self.COLUMNS
        )
        for column in self.COLUMNS:
            # Configuring video browser which contains playlist
            self.__video_browser.heading(
                VideosDB.COLUMNS[column], text=LibraryItem.HEADINGS[column]
            )
            self.__video_browser.column(
                VideosDB.COLUMNS[column], width=self.COLUMNS_WIDTH[column]
            )

    def _display_widgets(self):
        self.__video_browser.grid(row=0, column=3, sticky='nsew')
        self.__start_label.grid(row=1, column=0, sticky='es')
        self.__progress_slider.grid(row=1, column=1, sticky='wes')
        self.__end_label.grid(row=1, column=2, sticky='ws')
        self.__select_video_btn.grid(row=1, column=3, sticky='n')
        self.__play_btn.grid(row=2, column=1, sticky='n')
        for children in self.winfo_children():
            children.grid(padx=7, pady=7)

    def __time_to_str(self, seconds=0):
        """Convert time to string
        Args:
            seconds: videos duration in seconds
        Returns:
            a string of converted time
        """

        return str(datetime.timedelta(seconds=int(seconds)))

    def __clear_contents(self):
        """Clear the playlist contents"""

        for item in self.__video_browser.get_children():
            self.__video_browser.delete(item)

    def __refresh_playlist(self):
        """Display new playlist"""

        self.__clear_contents()
        for id, video in enumerate(self.__playlist.values()):
            self.__video_browser.insert(
                '', tk.END, iid=id, values=video.list_all(self.COLUMNS)
            )

        self.__video_browser.focus(0)  # Set the first video to be selected
        self.__video_browser.selection_set(0)  #

    def __on_close(self):
        self.withdraw()  # Hide without completely close the window

    def __add_video(self, video):
        """Add video to the current playlist"""

        self.__playlist.add(video)
        self.__refresh_playlist()

    def __update_duration(self, event):
        """Update new duration of playing videos"""

        duration = self.__player.video_info()['duration']
        self.__end_label['text'] = self.__time_to_str(duration)
        self.__progress_slider['to'] = duration

    def __update_scale(self, event):
        """Update the progress bar once every second"""

        self.__progress_value.set(self.__player.current_duration())

    def __video_ended(self, event):
        """Reset the progress bar and button when the video ended"""

        self.__play_btn['text'] = 'Play'
        self.__progress_slider.set(0)

    def __load_video(self, video):
        """Load new video

        Args:
            video - LibraryItem object
        """

        if self.__player:
            # Remove current playing video
            self.__player.destroy()
        self.__player = Player(
            self,
            duration=self.__update_duration,
            update_scale=self.__update_scale,
            video_ended=self.__video_ended,
        )  # create new video player object
        file_path = video.get_file_path()
        self.__player.load(file_path)
        self.__progress_slider.config(to=0, from_=0)  # Reset the progress bar
        self.__progress_value.set(0)  #

    def __seek(self, value):
        """Play video at a specific second

        Args:
            value - a time frame to play in seconds
        """
        self.__player.seek(int(float(value)))

    def __play_pause(self):
        """Toggle play button between Play-Pause"""

        if self.__player.is_paused():
            self.__player.play()
            self.__play_btn['text'] = 'Pause'
        else:
            self.__player.pause()
            self.__play_btn['text'] = 'Play'

    def __play_video(self):
        """Get the current selected video in playlist and play"""

        id = int(
            self.__video_browser.selection()[0]
        )  # Get the current selected video in playlist
        video = tuple(self.__playlist.values())[id]
        video.increment_play_count()  # Update play count
        self.__load_video(video)  # Load video to thread

    def play(self, playlist):
        if self.winfo_viewable():
            # ask to replacing new playlist if the mediaplayer has already been displayed
            replacing = msgbox.askokcancel(
                title='Replace playlist',
                message='Replace current playing playlist?',
                icon=msgbox.WARNING,
            )
            if not replacing:
                return
        self.__playlist = playlist  # replace the playlist
        self.__refresh_playlist()
        self.__play_video()
        self.deiconify()  # display the window


class Player(TkinterVideo):
    """Video player inherits from TkinterVideo class"""

    """
    @params:
        root - widgets root
        kwargs - event handlers
    """

    def __init__(self, root, **kwargs):
        super().__init__(root, scaled=True)
        self.bind(
            "<<Duration>>", kwargs.get('duration')
        )  # Called when new duration is loaded
        self.bind(
            "<<SecondChanged>>", kwargs.get('update_scale')
        )  # Called when video frame change
        self.bind(
            "<<Ended>>", kwargs.get('video_ended')
        )  # Called when video ended

        self.grid(row=0, column=0, columnspan=3, sticky='nsew')
