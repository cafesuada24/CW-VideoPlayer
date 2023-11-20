from dataclasses import dataclass

import tkinter as tk
from tkinter import ttk

from .widgets import *
from .core.videos_db import VideosDB
from .core.video_library import LibraryItemCollection

@dataclass(frozen=True)
class Constants:
    pass

@dataclass(frozen=False)
class DB:
    db = VideosDB()
    data = LibraryItemCollection.from_sequences(db.get_all())

@dataclass(frozen=False)
class Variable:
    selected_item = tk.IntVar() 

@dataclass(frozen=False)
class Widgets:
    MAIN_LAYOUT = None
    HEAD_BAR = None
    FOOTER = None
    BROWSER = None
    CHECK_VIDEOS_PANEL = None
    CREATE_VIDEO_LIST_PANEL = None
    UPDATE_VIDEO_PANEL = None
