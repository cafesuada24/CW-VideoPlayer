from ..singleton import SingletonMeta
from ..core.videos_db import VideosDB
from ..core.search_engine import SearchEngine
from ..core.video_library import LibraryItemCollection
from ..core.search_engine import SearchEngine


class General(metaclass=SingletonMeta):
    def __init__(self):
        data = VideosDB().cursor.execute('SELECT * FROM videos;')
        self.__data = LibraryItemCollection.from_sequences(data.fetchall())
        data = []
        for item in self.__data:
            data.extend(
                (
                    (item.get_name().lower(), item.get_id()),
                    (item.get_director().lower(), item.get_id()),
                )
            )
        self.__search_engine = SearchEngine(data)
        self.__play_list = LibraryItemCollection()

    @property
    def data(self):
        return self.__data

    @property
    def search_engine(self):
        return self.__search_engine

    @property
    def play_list(self):
        return self.__play_list
