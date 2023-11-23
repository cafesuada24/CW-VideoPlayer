from ..singleton import SingletonMeta
from ..core.videos_db import VideosDB
from ..core.video_library import LibraryItemCollection

class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.__db = VideosDB()
        self.__data = LibraryItemCollection.from_sequences(self.__db.get_all)
    
    @property
    def db(self):
        return self.__db

    @property
    def data(self):
        return self.__data

