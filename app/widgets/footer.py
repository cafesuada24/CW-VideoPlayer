from tkinter import *
from tkinter import ttk

class Footer(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.__back_btn = ttk.Button(self, text='Back', command=self.__back)
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        

        Label(self, text='Version 1.2').grid(row=0, column=1, sticky=E)
        self.__back_btn.grid(row=0, column=0, sticky=W)

    def __back(self):
        self._root().display_frame('main')

