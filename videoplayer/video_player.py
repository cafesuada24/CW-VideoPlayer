import sys
import traceback

from tkinter import *
from tkinter import ttk

from check_videos import CheckVideosFrame
from create_video_list import CreateVideoListFrame
from update_videos import UpdateVideosFrame

class MainFrame(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
         
        for column in range(3):
            self.columnconfigure(column, weight=1)

        self.__create_widgets()

    def __create_widgets(self):
        ttk.Label(
                self,
                text='Select an option by clicking one of the buttons below').grid(row=0, column=0, columnspan=3)
        
        ttk.Button(
                self,
                text='Check Videos',
                command=lambda: self._root()._display_frame('check_videos')
                ).grid(row=1, column=0, sticky=(W, E))
        ttk.Button(
                self,
                text='Create Video List',
                command=lambda: self._root()._display_frame('create_video_list')
                ).grid(row=1, column=1, sticky=(W, E))
        ttk.Button(
                self,
                text='Update Videos',
                command=lambda: self._root()._display_frame('update_videos')
                ).grid(row=1, column=2, sticky=(W, E))

        for widget in self.winfo_children():
            widget.grid(padx=5, pady=5)

class VideoPlayer(Tk):
    def __init__(self):
        super().__init__()
        self.title('Video Player')
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.resizable(width=False, height=False)

        self.__curr_frame = None
        self.frames = {}

        self.__create_widgets()
    
    def _display_frame(self, frame):
        try:
            frame = self.frames[frame]
        except KeyError as e:
            print(f'frame not found: {frame}', file=sys.stderr)
            traceback.print_stack(file=sys.stderr)
        else:
            if (self.__curr_frame is not None):
                self.__curr_frame.grid_forget()
            self.__curr_frame = frame
            self.__curr_frame.grid(column=0, row=0, sticky=(N, S, E, W))

    def __create_widgets(self):
        self.frames['main'] = MainFrame(self)
        self.frames['check_videos'] = CheckVideosFrame(self)
        self.frames['update_videos'] = UpdateVideosFrame(self)
        self.frames['create_video_list'] = CreateVideoListFrame(self)

        self._display_frame('main')

if __name__ == '__main__':
    video_player = VideoPlayer()
    video_player.mainloop()
