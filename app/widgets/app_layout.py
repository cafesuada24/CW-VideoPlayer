import tkinter as tk
from tkinter import ttk

from .. import CONFIG
from ..namespace import Widgets, Variable, General
from .video_browser import VideoBrowser
from .head_bar import HeadBar
from .footer import Footer
from .check_videos import CheckVideosPanel
from .create_video_list import CreateVideoListPanel
from .update_videos import UpdateVideoPanel
from ..core.search_engine import SearchEngine

COLUMNS = CONFIG['display']['columns']

class MainLayout(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        
        # Search engine init
        _data = []
        for item in General.data:
            _data.extend(((item.get_name().lower(), item.id), (item.get_director().lower(), item.id)))
        General.search_engine = SearchEngine(_data)
        
        # Initialize variables
        Variable.browser_data = list(General.data)
        Variable.selected_item = tk.IntVar()
        Variable.search_entry = tk.StringVar()
        
        # Initialize widgets
        Widgets.MAIN_LAYOUT = self
        Widgets.HEAD_BAR = HeadBar(self)
        Widgets.FOOTER = Footer(self)
        Widgets.BROWSER = VideoBrowser(self)
        Widgets.UPDATE_VIDEO_PANEL = UpdateVideoPanel(self)
        Widgets.CHECK_VIDEOS_PANEL = CheckVideosPanel(self)
        Widgets.CREATE_VIDEO_LIST_PANEL = CreateVideoListPanel(self)

        self._head_bar = None
        self._rpanel = None
        self._footer = None
        self._browser = None

        self.columnconfigure(0, weight=7)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=8)
        self.rowconfigure(2, weight=1)

    def display(self, head_bar=None, browser=None, rpanel=None, footer=None):
        if self._head_bar:
            self._head_bar.grid_forget()
        if self._browser:
            self._browser.grid_forget()
        if self._rpanel:
            self._rpanel.grid_forget()
        if self._footer:
            self._footer.grid_forget()
        self._head_bar = head_bar or Widgets.HEAD_BAR
        self._browser = browser or Widgets.BROWSER
        self._rpanel = rpanel
        self._footer = footer or Widgets.FOOTER
        self.__layout()
        self.grid(row=0, column=0, sticky=tk.NSEW)

    def __layout(self):
        self._head_bar.grid(row=0, column=0, sticky=tk.NSEW)
        self._browser.grid(row=1, column=0, sticky=tk.NSEW)
        self._rpanel.grid(row=0, column=1, rowspan=2, sticky=tk.NSEW)
        self._footer.grid(row=2, column=0, columnspan=2, sticky=tk.NSEW)
        for children in (self._head_bar, self._browser, self._rpanel, self._footer):
            children.grid(padx=5, pady=5)
        
