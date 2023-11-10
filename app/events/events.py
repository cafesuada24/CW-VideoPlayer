from tkinter.ttk import Frame

class Event:
    def __init__(self, caller: Frame):
        self._caller = caller
    
    @property
    def id(self) -> int:
        return self._caller._video_id.get()

    @property
    def videos(self):
        return self._caller.videos

    @property
    def db(self):
        return self._caller.db

class CheckButtonClickEvent(Event):
    def __init__(self, caller):
        super().__init__(caller)

    @property
    def output(self):
        return self._caller._display_info

class UpdateButtonClickEvent(Event):
    def __init__(self, caller):
        super().__init__(caller)

    @property
    def value(self) -> int | str:
        return self._caller._new_val.get()
    
    @property
    def column(self) -> str:
        return self._caller._update_column.get()

    @property
    def output(self):
        return self._caller._display_info

class PlaylistButtonClickEvent(Event):
    def __init__(self, caller):
        super().__init__(caller);
    
    @property
    def curr_playlist(self):
        return self._caller._curr_playlist

    @property
    def output(self):
        return self._caller._update_texts
