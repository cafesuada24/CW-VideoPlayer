from tkinter import *
from tkinter import ttk

from .. import CONFIG
from ..namespace import Widgets
from .video_browser import VideoBrowser
from .head_bar import HeadBar
from .footer import Footer
from .check_videos import CheckVideosPanel
from .create_video_list import CreateVideoListPanel
from .update_videos import UpdateVideoPanel

COLUMNS = CONFIG['display']['columns']

# class VideoFrame(ttk.Frame):
#     def __init__(self, root):
#         super().__init__(root)
#         self._video_id = IntVar()
#         self.__info_text = None
#         self.__table = None
#         self.se = self._root().se
#         self.columnconfigure(0, weight=1)
#         self.columnconfigure(1, weight=6)
#         self.columnconfigure(2, weight=3)
#         self.rowconfigure(0, weight=1)
#         for row in range(1, 9):
#             self.rowconfigure(row, weight=2)
#         self.__render_base_form()
#         self.__bind_default_events()
#         self._create_widgets()
#         self._bind_events()
#         self.__align()
#
#     @property
#     def _number_input_validate(self):
#         def __validator(input):
#             return input == '' or input.isdigit()
#         return (self.register(__validator), '%P')
#     
#     @property
#     def videos(self):
#         return self._root().videos
#     
#     @property
#     def db(self):
#         return self._root().db
#
#     def __render_base_form(self):
#         ttk.Button(
#                 self,
#                 text='List All Videos',
#                 width=25,
#                 command=self.__display_videos
#             ).grid(column=0, row=0, sticky=(W, S))
#         ttk.Button(
#                 self,
#                 text='Back',
#                 command=self.__back_to_mainframe
#             ).grid(column=0, row=9, sticky=(W, S))
#         
#     
#         # Search bar
#         self.__search_bar_text = StringVar()
#         self.__search_bar = ttk.Entry(self, textvariable=self.__search_bar_text)
#         self.__search_bar.grid(row=0, column=1, sticky=(W,E))
#         # ---------
#         
#         # Table
#         self.__table = ttk.Treeview(self, columns=COLUMNS['id'], show='headings', height=20)
#         for col, name in zip(COLUMNS['id'], COLUMNS['heading']):
#             self.__table.heading(col, text=name)
#         self.__table.grid(column=0, row=1, columnspan=2, rowspan=8, sticky=(N, W, E, S))
#         # ---------
#
#         self.__info_text = Text(self, height=7, width=35)
#         self.__info_text['state'] = 'disable'
#         self.__info_text.grid(row=1, column=2, sticky=(N, W, E, S))
#         
#     def __back_to_mainframe(self):
#         self._root()._display_frame('main')
#     
#     def __clear_table(self):
#         for item in self.__table.get_children():
#             self.__table.delete(item)
#
#     def __display_videos(self, *ignore):
#         self.__clear_table()
#         for id in self.se.search_prefix(self.__search_bar_text.get().lower()):
#             self.__table.insert('', END, values=self.videos[id].list_all())
#
#     def __bind_default_events(self):
#         self.__table.bind('<<TreeviewSelect>>', self.__item_selected)
#         self.__search_bar.bind('<Return>', self.__display_videos)
#
#     def __item_selected(self, event):
#         selected = self.__table.selection()
#         if not selected: return
#
#         item = selected[0]
#         id = self.__table.item(item)['values'][0]
#         self._video_id.set(id)
#
#     def __align(self):
#         for widget in self.winfo_children():
#             widget.grid(padx=5, pady=5)
#
#     def _display_info(self, content):
#         self.__info_text['state'] = 'normal'
#         self.__info_text.delete('1.0', 'end')
#         self.__info_text.insert('1.0', content)
#         self.__info_text['state'] = 'disable'
#
#     def _create_widgets(self):
#         raise NotImplementedError('this must be implemented')
#     
#     def _bind_events(self):
#         raise NotImplementedError('this must be implemented')
# class Singleton(type):
#     _instances = None
#     def __call__(cls, *args, **kwargs):
#         if not cls._instances:
#             cls._instances = super(Singleton, cls).__call__(*args, **kwargs)
#         return cls._instances

class MainLayout(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        
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
        self.grid(row=0, column=0, sticky=NSEW)

    def __layout(self):
        self._head_bar.grid(row=0, column=0, sticky=NSEW)
        self._browser.grid(row=1, column=0, sticky=NSEW)
        self._rpanel.grid(row=0, column=1, rowspan=2, sticky=NSEW)
        self._footer.grid(row=2, column=0, columnspan=2, sticky=NSEW)
        for children in (self._head_bar, self._browser, self._rpanel, self._footer):
            children.grid(padx=5, pady=5)
        
