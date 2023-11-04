from tkinter import *
from tkinter import ttk

class VideoFrame(ttk.Frame):
    def __init__(self, root, db):
        super().__init__(root)
        self._db = db
        self._columns = ('id', 'name', 'director', 'rate')
        self._info_text = None
        self._video_id = StringVar()
        self.__table = None
        self.columnconfigure(0, weight=6)
        self.columnconfigure(1, weight=4)
        self.rowconfigure(0, weight=1)
        for row in range(1, 9):
            self.rowconfigure(row, weight=2)
        self.__render_base_form()
        self.__bind_default_events()
    
    def __render_base_form(self):
        ttk.Button(
                self,
                text='List All Videos',
                width=25,
                command=self.__display_videos
                ).grid(column=0, row=0, sticky=(W, S))

        column_names = ('Number', 'Name', 'Director', 'Ratings')
        self.__table = ttk.Treeview(self, columns=self._columns, show='headings', height=20)
        for col, name in zip(self._columns, column_names):
            self.__table.heading(col, text=name)
        self.__table.grid(column=0, row=1, rowspan=8, sticky=(N, W, E, S))
        
        self._info_text = Text(self, height=7, width=35)
        self._info_text['state'] = 'disable'
        self._info_text.grid(row=1, column=1, sticky=(N, W, E, S))
        
        for widget in self.winfo_children():
            widget.grid(padx=5, pady=5)
    
    def __clear_table(self):
        for item in self.__table.get_children():
            self.__table.delete(item)
        self.update()

    def __display_videos(self):
        self.__clear_table()
        for video in self._db.list_all():
            values = (video.id, video.name, video.director, video.rating)
            self.__table.insert('', END, values=values)
        self.update()

    def __bind_default_events(self):
        self.__table.bind('<<TreeviewSelect>>', self.__item_selected)

    def __item_selected(self, event):
        # for selected_item in self.__table.selection():
        #     item = self.__table.item(selected_item)
        #     id = item['values'][0]
        #     self._video_id.set(id)
        item = self.__table.item(self.__table.focus())
        id = item['values'][0]
        self._video_id.set(id)


    def _insert_info(self, content):
        self._info_text['state'] = 'normal'
        self._info_text.delete('1.0', 'end')
        self._info_text.insert('1.0', content)
        self._info_text['state'] = 'disable'

    def _create_widgets(self):
        raise NotImplementedError
    
    @property
    def _number_input_validate(self):
        def __validator(input):
            return input == '' or input.isdigit()
        return (self.register(__validator), '%P')
