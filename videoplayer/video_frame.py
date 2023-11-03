from tkinter import *
from tkinter import ttk

class VideoFrame(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        
        self._columns = ('id', 'name', 'author', 'rate')
        self._info_text = None
        self.rowconfigure(0, weight=1)
        # self.rowconfigure(1, weight=2)
        for row in range(1, 9):
            self.rowconfigure(row, weight=2)
        self.columnconfigure(0, weight=6)
        self.columnconfigure(1, weight=4)
        
        self.__render_base_form()
    
    def __render_base_form(self):
        ttk.Button(
                self,
                text='List All Videos',
                width=25
                ).grid(column=0, row=0, sticky=(W, S))

        column_names = ('Number', 'Name', 'Author', 'Ratings')
        tree = ttk.Treeview(self, columns=self._columns, show='headings', height=20)
        for col, name in zip(self._columns, column_names):
            tree.heading(col, text=name)
        tree.grid(column=0, row=1, rowspan=8, sticky=(N, W, E, S))
        
        self._info_text = Text(self, height=7, width=35)
        self._info_text['state'] = 'disable'
        self._info_text.grid(row=1, column=1, sticky=(N, W, E, S))
        
        for widget in self.winfo_children():
            widget.grid(padx=5, pady=5)

    def _create_widgets(self):
        raise NotImplementedError

    def _insert_info(self, content):
        self._info_text['state'] = 'normal'
        self._info_text.delete('1.0', 'end')
        self._info_text.insert('1.0', content)
        self._info_text['state'] = 'disable'
