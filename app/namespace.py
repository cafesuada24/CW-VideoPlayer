from dataclasses import dataclass
from tkinter import ttk
import tkinter as tk

from .widgets import *
from .core.videos_db import VideosDB
from .core.video_library import LibraryItemCollection
from .core.search_engine import SearchEngine

class Constants:
    pass

# This class contains General purposes variables
class General:
    db = VideosDB()
    data = LibraryItemCollection.from_sequences(db.get_all())
    search_engine = None

# This class contains Tkinter variables and related functions
class Variable:
    selected_item = None 
    search_entry = None
    current_playlist = dict()

class Widgets:
    MAIN_LAYOUT = None
    HEAD_BAR = None
    FOOTER = None
    BROWSER = None
    CHECK_VIDEOS_PANEL = None
    CREATE_VIDEO_LIST_PANEL = None
    UPDATE_VIDEO_PANEL = None

# This class contains functions to handle widgets's events and commands
class EventHandler:
    pass

def init_namespaces():
    pass
