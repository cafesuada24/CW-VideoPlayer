import sqlite3 as sql
from collections.abc import Sequence 

from videos_db import VideosDB, UpdateTransaction

class Video:
    def __init__(self, id, name, director, rating, play_count, path):
        self.id = int(id)
        self.name = name
        self.director = director
        self.rating = int(rating)
        self.play_count = int(play_count)
        self.path = path
    
    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        if key not in self.__dict__:
            raise KeyError(f'column not found: {key}')
        self.__dict__[key] = value

class VideoCollection:
    def __init__(self, videos: Sequence[Video] = None):
        if videos is None:
            videos = []
        videos = {video.id: video for video in videos}
        self.__videos = videos
    
    @classmethod
    def from_sequences(cls, videos: Sequence[Sequence]):
        videos = (Video(*video) for video in videos)
        return cls(videos)
    
    def add(self, video: Video) -> None:
        if type(video) is not Video:
           video = Video(*video) 
        self.__videos[video.id] = video
    
    def remove(self, id: int):
        del self.__videos[id]

    def __getitem__(self, video_id):
        return self.__videos[video_id]

    def __iter__(self):
        return iter(self.__videos.values())

class LibraryItem:
    def __init__(self):
        self.__db = VideosDB()
        self.__videos = None
        self.__transactions = []
        with self.__db as cursor:
            query = 'SELECT * FROM videos;'
            cursor.execute(query)
            videos_ = cursor.fetchall()
            self.__videos = VideoCollection.from_sequences(videos_)
    
    def __del__(self):
        if not self.__transactions: return

        with self.__db as cursor:
            for tsx in self.__transactions:
                query = f'''
                    UPDATE {self.__db.TABLE_NAME}
                    SET {tsx.column} = ?
                    WHERE video_id = ?;
                    '''
                cursor.execute(query, (tsx.value, tsx.id))

    @property
    def UPDATABLE(self):
        return ('name', 'director', 'rating')
    
    @property
    def TYPES(self):
        types = (str, str, int)
        return {tp: col for tp, col in zip(self.UPDATABLE, types)}

    def update(self, id: int, column: str, value: str) -> None:
        value = self.TYPES[column](value)
        self.get_video_by_id(id)[column] = value
        self.__transactions.append(UpdateTransaction(column, value, id))

    def get_video_by_id(self, id) -> Video:
        return self.__videos[id]

    def list_all(self) -> VideoCollection:
        return self.__videos
        
    def get_name(self, id: int) -> str:
        return self.__videos[id].name

    def get_director(self, id: int) -> str:
        return self.__videos[id].director

    def get_rating(self, id: int) -> str:
        return self.__videos[id].rating

    def set_rating(self, id: int, new_rating: int) -> None:
        self.__videos[id].rating = new_rating

    def get_play_count(self, id: int) -> str:
        return self.__videos[id].play_count
    
    def increment_play_count(self, id: int) -> None:
        play_count = self.get_play_count(id) + 1
        self.update(id, 'play_count', play_count)
