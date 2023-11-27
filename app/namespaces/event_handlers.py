# from .widgets import Widgets
import tkinter as tk
from .tk_variable import TkVariable
from .general import General
from ..core.video_library import LibraryItem


class EventHandlers:
    @staticmethod
    def get_brower_items():
        _prefix = TkVariable().get_search_entry()
        _data = General().search_engine.search_prefix(_prefix)
        _data = (General().data[id] for id in _data)
        d = {
            'id': 'video_id',
            'author': 'director',
            'name': 'name',
            'rating': 'rating',
        }
        sort_by = TkVariable().get_sort_by()
        sort_order = TkVariable().get_sort_order()
        return sorted(
            _data, key=lambda val: val[d[sort_by]], reverse=sort_order
        )

    @staticmethod
    def get_video_info():
        id = TkVariable().get_selected_id()
        if not id:
            return None
        data = General().data[id]
        return data.list_all(LibraryItem.COLUMNS[1:])

    @staticmethod
    def add_selected_to_playlist():
        id = TkVariable().get_selected_id()
        if not id or id in General().play_list:
            return False
        item = General().data[id]
        General().play_list.add(item)
        return True

    @staticmethod
    def remove_selected_from_playlist():
        id = TkVariable().get_selected_id()
        if not id or id not in General().play_list:
            return False
        General().play_list.remove(id)
        return True

    @staticmethod
    def play_playlist():
        if not General().play_list:
            return False
        General().play_list.play()
        return True

    @staticmethod
    def update_video(self):
        try:
            id = Variable.selected_item.get()
            name, director, path = self.__inputs[1:]
            name = name.get()
            director = director.get()
            path = path.get()
            origin = General().data[id]
            if name != origin.get_name():
                origin['name'] = name
                General().db.update(id, 'name', name)
            if director != origin.get_director():
                origin['director'] = director
                General().db.update(id, 'director', director)
            if path != origin.get_file_path():
                origin['file_path'] = path
                General().db.update(id, 'file_path', path)
        except Exception as e:
            print(e)
            pass
