import sqlite3 as sql
from collections.abc import Sequence 

from .. import CONFIG

class LibraryItem:
    def __init__(self, id, name, director, rating, play_count, path):
        self.__data = {
            'video_id': int(id),
            'name': name,
            'director': director,
            'rating': int(rating),
            'play_count': int(play_count),
            'file_name': path
            }
    
    def list_all(self, attrs: Sequence[str] = CONFIG['database']['columns']) -> tuple[int | str]:
        return tuple(self.__data[attr] for attr in attrs) 
    
    @property
    def id(self) -> int:
        return self.__data['video_id']

    def get_name(self) -> str:
        return self.__data['name']

    def get_director(self) -> str:
        return self.__data['director']

    def get_rating(self) -> int:
        return self.__data['rating']

    def get_play_count(self) -> int:
        return self.__data['play_count']

    def set_rating(self, new_rating: int) -> None:
        self.__data['rating'] = new_rating
    
    def increment_play_count(self) -> None:
        self.__data['play_count'] += 1 

    def __setitem__(self, item, new_val):
        if item not in self.__data:
            raise AttributeError("can't assign new attribue")
        self.__data[item] = type(self.__data[item])(new_val)


class LibraryItemCollection:
    def __init__(self, videos: Sequence[LibraryItem] = None):
        if videos is None:
            videos = hash()
        videos = {video.id: video for video in videos}
        self.__videos = videos
    
    @classmethod
    def from_sequences(cls, videos: Sequence[Sequence]):
        videos = (LibraryItem(*video) for video in videos)
        return cls(videos)
    
    def add(self, video: LibraryItem) -> None:
        self.__videos[video.id] = video
    
    def remove(self, id: int) -> None:
        del self.__videos[id]

    def __getitem__(self, video_id) -> Video:
        return self.__videos[video_id]

    def __iter__(self):
        return iter(self.__videos.values())
