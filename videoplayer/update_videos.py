from tkinter import *
from tkinter import ttk

from video_frame import VideoFrame

class UpdateVideosFrame(VideoFrame):
    def __init__(self, root):
        super().__init__(root)

        self._create_widgets()

    def _create_widgets(self):
        ttk.Label(self, text='Status').grid(column=1, row=0, sticky=S)
        ttk.Label(
                self,
                text='Enter movie number or name:'
                ).grid(pady=5, column=1, row=2, sticky=(W, S))
        ttk.Label(
                self,
                text='Select attribute:'
                ).grid(column=1, row=4, sticky=(W, S))
        ttk.Label(self, text='Enter new value:').grid(column=1, row=6, sticky=(W, S))

        video_entry = ttk.Entry(self, width=35)
        video_entry.grid(row=3, column=1, sticky=(N, W, E, S))
        video_entry.focus()
        
        combobox = ttk.Combobox(self)
        combobox['state'] = 'readonly'
        combobox['values'] = self._columns
        combobox.set('rate') 
        combobox.grid(pady=5, column=1, row=5, sticky=(W, E, N))
        
        new_val_entry = ttk.Entry(self, width=35)
        new_val_entry.grid(row=7, column=1, sticky=(N, W, E, S))
        ttk.Button(
                self,
                text='Update',
                width=20
                ).grid(pady=5, row=8, column=1, sticky=(N, W, E, S))
        
        for widget in self.winfo_children():
           widget.grid(padx=5)
