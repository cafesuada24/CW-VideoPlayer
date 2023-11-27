import tkinter as tk
from tkinter import ttk


class AppFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self._create_widgets()
        self._display_widgets()

        for children in self.winfo_children():
            children.grid(padx=7, pady=7)

    def _create_widgets(self):
        raise NotImplementedError(
            '_create_widgets: expected to be implemented'
        )

    def _display_widgets(self):
        raise NotImplementedError(
            '_display_widgets: expected to be implemented'
        )


class InfoText(tk.Text):
    def __init__(self, root):
        super().__init__(root, height=1, width=35)
        self['state'] = 'disabled'

    def display(self, value: str) -> None:
        self['state'] = 'normal'
        self.delete('1.0', tk.END)
        self.insert('1.0', value)
        self['state'] = 'disabled'
