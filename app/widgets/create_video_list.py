from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msgbox

from app.core.video_library import LibraryItemCollection
from ..namespace import Widgets
from ..events.event_handlers import EventHandler
from ..events.events import PlaylistButtonClickEvent 
from ..namespace import Variable, General

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

        attrs = ('Name',)
        ttk.Label(self, text='ID  ').grid(row=3, column=0, sticky=W)
        self.__id_entry = ttk.Entry(self, textvariable=Variable.selected_item)
        self.__id_entry.grid(row=3, column=1, ipady=3, sticky=NSEW)
        ttk.Separator(self, orient='horizontal').grid(column=0, columnspan=2, sticky=NSEW)
        self.__field = []
        for row, attr in zip(range(5, len(attrs) * 2 + 5, 2), attrs):
            ttk.Label(self, text=attr).grid(row=row, column=0, sticky=W)
            text = ttk.Entry(self)
            text.grid(row=row, column=1, ipady=3, sticky=NSEW)
            self.__field.append(text)
            ttk.Separator(self, orient='horizontal').grid(column=0, columnspan=2, sticky=NSEW)
        
        self.__add_btn = ttk.Button(self, text='Add', width=20, command=self.add_selected)
        self.__remove_btn = ttk.Button(self, text='Remove', width=20, command=self.remove_selected)
        self.__play_btn = ttk.Button(self, text='Play playlist', command=self.play_playlist)
        
        self.__add_btn.grid(column=0, row=7, columnspan=2, sticky=W)
        self.__remove_btn.grid(column=1, row=7, sticky=E)
        self.__play_btn.grid(column=0, columnspan=2, sticky=(W, E))

        for children in self.winfo_children():
            children.grid(padx=5, pady=5)

    def display_playlist(self, items):
        self.__list.delete(0, END)
        self.__list.insert(END, *(f"{id} - {item.get_name()}" for id, item in items.items()))

    def add_selected(self):
        try:
            id = Variable.selected_item.get()
            if id not in Variable.current_playlist:
                Variable.current_playlist[id] = General.data[id]
        except Exception as e:
            print(e)
            msgbox.showerror('Invalid ID', message='Invalid ID')
        self.display_playlist(Variable.current_playlist)
            
    def remove_selected(self):
        try:
            id = Variable.selected_item.get()
            del Variable.current_playlist[id]
        except Exception as e:
            print(e)
            msgbox.showerror('Invaid Id', message='Invalid ID')
        self.display_playlist(Variable.current_playlist)

    def play_playlist(self):
        if not Variable.current_playlist:
            msgbox.showerror('Playlist error', message='No video to play!')
            return

        for item in Variable.current_playlist.values():
            item.increment_play_count()
            General.db.update(item.id, 'play_count', item.get_play_count())
        msgbox.showinfo('Playing...', message='Played')

