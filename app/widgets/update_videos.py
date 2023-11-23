from tkinter import *
from tkinter import ttk

from ..events.events import UpdateButtonClickEvent 
from ..events.event_handlers import EventHandler
from ..namespaces.tk_variable import TkVariable

class UpdateVideoPanel(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        
        TkVariable().selected_id.trace_add('write', self.display_info)

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=3)

        ttk.Label(self, text='Update Video').grid(row=0, column=0, columnspan=2)
        ttk.Separator(self, orient='horizontal').grid(row=1, column=0, columnspan=2, sticky=NSEW)

        attrs = ('Id', 'Name', 'Director', 'Path')
        self.__vars = (TkVariable().selected_id, StringVar(), StringVar(), StringVar())
        self.__inputs = []
        for row, attr, var in zip(range(2, len(attrs) * 2 + 2, 2), attrs, self.__vars):
            ttk.Label(self, text=attr).grid(row=row, column=0, sticky=W)
            input = ttk.Entry(self, width=30, textvariable=var)
            input.grid(row=row, column=1, ipady=3, sticky=E)
            self.__inputs.append(input)
            ttk.Separator(self, orient='horizontal').grid(row=row+1, column=0, columnspan=2, sticky=NSEW)
        button = ttk.Button(self, text='Update', width=20, command=EventHandler().update_video)
        button.grid(row=10, column=1, sticky=E)

        for children in self.winfo_children():
            children.grid(padx=5, pady=5)
    
    def display_info(self, *ignore):
        try:
            id = Variable.selected_item.get()
            data = General.data[id]
            data = (data.get_name(), data.get_director(), data.get_file_path())
            for idx in range(0, len(data)):
                self.__vars[idx+1].set(data[idx])
        except Exception as e:
            print(e)

    
            
