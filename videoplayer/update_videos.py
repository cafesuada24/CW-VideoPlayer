from tkinter import *
from tkinter import ttk

from video_frame import VideoFrame

class UpdateVideosFrame(VideoFrame):
    def __init__(self, root, db):
        super().__init__(root, db)
        self.__new_val = StringVar()
        self.__update_column = StringVar()
        self._create_widgets()

    def _create_widgets(self):
        ttk.Label(self, text='Status').grid(column=1, row=0, sticky=S)
        ttk.Label(
                self,
                text='Enter movie number:'
                ).grid(pady=5, column=1, row=2, sticky=(W, S))
        ttk.Label(
                self,
                text='Select attribute:'
                ).grid(column=1, row=4, sticky=(W, S))
        ttk.Label(self, text='Enter new value:').grid(column=1, row=6, sticky=(W, S))

        video_entry = ttk.Entry(
                self,
                width=35,
                textvariable=self._video_id,
                validate='key',
                validatecommand=self._number_input_validate
                )
        video_entry.grid(row=3, column=1, sticky=(N, W, E, S))
        video_entry.focus()
        
        combobox = ttk.Combobox(self, textvariable=self.__update_column)
        combobox['state'] = 'readonly'
        combobox['values'] = self._db.UPDATABLE
        combobox.set('rating') 
        combobox.grid(pady=5, column=1, row=5, sticky=(W, E, N))
        
        new_val_entry = ttk.Entry(
                self,
                width=35,
                textvariable=self.__new_val
                )
        new_val_entry.grid(row=7, column=1, sticky=(N, W, E, S))
        ttk.Button(
                self,
                text='Update',
                width=20,
                command=self.__update
                ).grid(pady=5, row=8, column=1, sticky=(N, W, E, S))
        
        for widget in self.winfo_children():
           widget.grid(padx=5)

    def __update(self):
        id = self._video_id.get()
        value = self.__new_val.get()
        column = self.__update_column.get()
        
        if value == '':
            self._display_info('Value can not be empty')
            return

        try:
            self._db.update(id, column, value)
            self.update()
            self._display_info('Updated!')
        except KeyError as e:
            self._display_info(f'Video id not found: {e}') 
        except ValueError as e:
            self._display_info(f'Invalid value "{value}" for "{column}"')
