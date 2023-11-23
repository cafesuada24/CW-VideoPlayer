# from . import Variable, Widgets

class EventHandlers:
    @staticmethod
    def update_brower_items():
        # _prefix = Variable.search_entry.get().strip().lower()
        # _ids = General.search_engine.search_prefix(_prefix)
        # _data = [General.data[id] for id in _ids] 
        # d = {'id': 'video_id', 'author': 'director', 'name': 'name', 'rating': 'rating'}
        # sort_by = self.__sort_by_var.get().strip().lower()
        # sort_order = self.__sort_order_var.get().strip().lower()
        # _data.sort(key=lambda val: val[d[sort_by]], reverse=sort_order=='descending')
        # Widgets.BROWSER.display_items(_data)
        pass

    @staticmethod
    def show_info(self, *ignore):
        # try:
        #     id = Variable.selected_item.get()
        #     data = General.data[id]
        #     self.display_info(data.list_all(('name', 'director', 'rating', 'play_count', 'file_path')))
        # except:
        #     msgbox.showerror('Id error', message='Invalid ID')
        pass

    @staticmethod
    def add_selected(self):
        try:
            id = Variable.selected_item.get()
            if id not in Variable.current_playlist:
                Variable.current_playlist[id] = General.data[id]
        except Exception as e:
            print(e)
            msgbox.showerror('Invalid ID', message='Invalid ID')
        self.display_playlist(Variable.current_playlist)
    
    @staticmethod
    def remove_selected(self):
        try:
            id = Variable.selected_item.get()
            del Variable.current_playlist[id]
        except Exception as e:
            print(e)
            msgbox.showerror('Invaid Id', message='Invalid ID')
        self.display_playlist(Variable.current_playlist)
    
    @staticmethod
    def play_playlist(self):
        if not Variable.current_playlist:
            msgbox.showerror('Playlist error', message='No video to play!')
            return

        for item in Variable.current_playlist.values():
            item.increment_play_count()
            General.db.update(item.id, 'play_count', item.get_play_count())
        msgbox.showinfo('Playing...', message='Played')

