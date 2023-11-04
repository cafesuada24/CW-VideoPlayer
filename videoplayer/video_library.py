import sqlite3 as sql

from videos_db import VideosDB

class Video:
    def __init__(self, id, name, director, rating, play_count, path):
        self.id = int(id)
        self.name = name
        self.director = director
        self.rating = int(rating)
        self.play_count = int(play_count)
        self.path = path

    def increase_play_count(self):
        self.play_count += 1

class VideoCollection:
    def __init__(self, videos: list):
        videos = (Video(*video) if type(video) is not Video else video for video in videos)
        videos = {video.id: video for video in videos}
        self.__videos = videos
    
    def add(self, video) -> None:
        if type(video) is not Video:
           video = Video(*video) 
        self[video.id] = video
    
    def remove(self, video: Video):
        if (video.id in self.__videos):
            del self.__videos[video.id]

    def __getitem__(self, video_id):
        return self.__videos[video_id]

    def __iter__(self):
        return iter(self.__videos.values())

class LibraryItem:
    def __init__(self):
        self.__db = VideosDB()
        self.__videos = None
        with self.__db as cursor:
            query = 'SELECT * FROM videos;'
            cursor.execute(query)
            videos_ = cursor.fetchall()
            self.__videos = VideoCollection(videos_)

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
        self.__videos[id].increase_play_count()

if __name__ == '__main__':
    lib = LibraryItem()
    print(lib.list_all())
