"""
This module contains classes that are designed for in
"""

import tkinter as tk
from tkinter import ttk


class AppFrame(tk.Frame):
    """Base class for every Tkinter Frames in the application"""

    def __init__(self, root):
        super().__init__(root)

        self._create_widgets()
        self._display_widgets()

        for children in self.winfo_children():
            children.grid(padx=7, pady=7)

    def _create_widgets(self):
        """Initialize all children widgets"""

        raise NotImplementedError(
            '_create_widgets: expected to be implemented'
        )

    def _display_widgets(self):
        """Display all created widgets"""

        raise NotImplementedError(
            '_display_widgets: expected to be implemented'
        )


class InfoText(tk.Text):
    """Base class for Text which are designed only for containing information"""

    def __init__(self, root):
        super().__init__(root, height=1, width=35)

        self[
            'state'
        ] = 'disabled'  # Infomation texts are not allowed to change

    def display(self, value: str) -> None:
        """Display information into Textbox

        Args:
            value: an information string to be displayed

        Returns:
            None
        """

        self['state'] = 'normal'
        self.delete('1.0', tk.END)  # Remove all contents
        self.insert('1.0', value)  # Display new contents
        self['state'] = 'disabled'
