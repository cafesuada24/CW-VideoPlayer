from dataclasses import dataclass

import tkinter as tk
from tkinter import ttk

from .widgets import *
from .core.videos_db import VideosDB
from .core.video_library import LibraryItemCollection
from .core.search_engine import SearchEngine

@dataclass(frozen=True)
class Constants:
    pass

@dataclass(frozen=False)
class General:
    db = VideosDB()
    data = LibraryItemCollection.from_sequences(db.get_all())
    search_engine = None

@dataclass(frozen=False)
class Variable:
    selected_item = None 
    search_entry = None

@dataclass(frozen=False)
class Widgets:
    MAIN_LAYOUT = None
    HEAD_BAR = None
    FOOTER = None
    BROWSER = None
    CHECK_VIDEOS_PANEL = None
    CREATE_VIDEO_LIST_PANEL = None
    UPDATE_VIDEO_PANEL = None
