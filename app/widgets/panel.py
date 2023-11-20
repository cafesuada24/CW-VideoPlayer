from tkinter import *
from tkinter import ttk

class CheckVideosPanel(ttk.Frame):    
    def __init__(self, root):
        super().__init__(root)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        # self.rowconfigure(0, weight=1) 

        ttk.Label(self, text='Video Infomation').grid(row=0, column=0, columnspan=2, sticky=(N, S))
        ttk.Separator(self, orient='horizontal').grid(row=1, column=0, columnspan=2, sticky=NSEW)

        attrs = ('Number', 'Name', 'Director', 'Play count', 'File path')
        for row, attr in zip(range(2, len(attrs) * 2 + 2, 2), attrs):
            # self.rowconfigure(row, weight=1)
            # self.rowconfigure(row + 1, weight=1)
            ttk.Label(self, text=attr).grid(row=row, column=0, sticky=W)
            Text(self, height=1, width=50).grid(row=row, column=1, ipady=3, sticky=(W, E))
            ttk.Separator(self, orient='horizontal').grid(row=row+1, column=0, columnspan=2, sticky=NSEW)

            # ttk.Frame(self).pack(side=TOP)
            # ttk.Label(self, text=f'{attr}: ').pack(side=LEFT)
            # Text(self, height=1).pack(side=RIGHT)
            # ttk.Separator(self, orient='horizontal').pack(side=TOP)
        self.__check_btn = ttk.Button(self, text='Check Videos', width=25)
        self.__check_btn.grid(column=1, sticky=(E, N, S))

        for children in self.winfo_children():
            children.grid(padx=7, pady=7)
            
class UpdateVideoPanel(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=3)

        ttk.Label(self, text='Update Video').grid(row=0, column=0, columnspan=2)
        ttk.Separator(self, orient='horizontal').grid(row=1, column=0, columnspan=2, sticky=NSEW)

        attrs = ('Number', 'Name', 'Director', 'Path')
        for row, attr in zip(range(2, len(attrs) * 2 + 2, 2), attrs):
            ttk.Label(self, text=attr).grid(row=row, column=0, sticky=W)
            input = ttk.Entry(self, width=30).grid(row=row, column=1, ipady=3, sticky=E)
            ttk.Separator(self, orient='horizontal').grid(row=row+1, column=0, columnspan=2, sticky=NSEW)
        button = ttk.Button(self, text='Update', width=20)
        button.grid(row=10, column=1, sticky=E)

        for children in self.winfo_children():
            children.grid(padx=5, pady=5)

class CreateVideoListPanel(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=3)

        ttk.Label(self, text='Create Video List').grid(row=0, column=0, columnspan=2)
        ttk.Separator(self, orient='horizontal').grid(row=1, column=0, columnspan=2, sticky=NSEW)
        
        var = Variable()
        self.__list = Listbox(self, width=50)
        self.__list.grid(row=2, column=0, columnspan=2)

        attrs = ('Number', 'Name')
        for row, attr in zip(range(3, len(attrs) * 2 + 3, 2), attrs):
            ttk.Label(self, text=attr).grid(row=row, column=0, sticky=W)
            input = ttk.Entry(self)
            input.grid(row=row, column=1, ipady=3, sticky=NSEW)
            ttk.Separator(self, orient='horizontal').grid(column=0, columnspan=2, sticky=NSEW)
        
        self.__add_btn = ttk.Button(self, text='Add', width=20)
        self.__remove_btn = ttk.Button(self, text='Remove', width=20)
        self.__play_btn = ttk.Button(self, text='Play playlist')
        
        self.__add_btn.grid(column=0, row=7, columnspan=2, sticky=W)
        self.__remove_btn.grid(column=1, row=7, sticky=E)
        self.__play_btn.grid(column=0, columnspan=2, sticky=(W, E))

        for children in self.winfo_children():
            children.grid(padx=5, pady=5)
