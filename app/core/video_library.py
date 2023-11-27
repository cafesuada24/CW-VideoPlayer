import sqlite3 as sql
from collections.abc import Sequence


class LibraryItem:
    COLUMNS = (
        'video_id',
        'name',
        'director',
        'rating',
        'play_count',
        'file_path',
    )
    HEADINGS = ('ID', 'Name', 'Director', 'Rating', 'Play Count', 'File Path')

    def __init__(
        self,
        id: int,
        name: str,
        director: str,
        rating: float,
        play_count: int,
        path: str,
    ):
        values = (
            int(id),
            str(name),
            str(director),
            float(rating),
            int(play_count),
            str(path),
        )
        self.__data = {key: val for key, val in zip(self.COLUMNS, values)}

    def list_all(
        self, attrs: Sequence[str | int] = COLUMNS
    ) -> tuple[int | str]:
        return tuple(self[attr] for attr in attrs)

    def get_id(self) -> int:
        return self.__data[self.COLUMNS[0]]

    def get_name(self) -> str:
        return self.__data[self.COLUMNS[1]]

    def get_director(self) -> str:
        return self.__data[self.COLUMNS[2]]

    def get_rating(self) -> int:
        return self.__data[self.COLUMNS[3]]

    def get_play_count(self) -> int:
        return self.__data[self.COLUMNS[4]]

    def get_file_path(self) -> str:
        return self.__data[self.COLUMNS[5]]

    def increment_play_count(self) -> None:
        self.__data[self.COLUMNS[4]] += 1

    def set_name(self, name: str) -> None:
        self.__data[self.COLUMNS[1]] = str(name)

    def sef_director(self, director: str) -> None:
        self.__data[self.COLUMNS[2]] = str(director)

    def set_rating(self, rating: float) -> None:
        self.__data[self.COLUMNS[3]] = float(rating)

    def set_file_path(self, file_path: str) -> None:
        self.__data[self.COLUMNS[5]] = str(file_path)

    def play(self):
        self.increment_play_count()

    def __getitem__(self, item: str) -> str | int:
        if isinstance(item, int):
            item = self.COLUMNS[item]
        if item not in self.__data:
            raise AttributeError(f'invalid attribute: {item}')
        return self.__data[item]

    def __setitem__(self, item: str, new_val: str | int) -> None:
        if isinstance(item, int):
            item = self.COLUMNS[item]
        if item not in self.__data:
            raise AttributeError('can\'t assign new attribue')
        self.__data[item] = type(self.__data[item])(new_val)

    def save(self):
        pass


class LibraryItemCollection:
    def __init__(self, videos: Sequence[LibraryItem] = None):
        if videos is None:
            videos = dict()
        videos = {video.get_id(): video for video in videos}
        self.__videos = videos

    @classmethod
    def from_sequences(cls, videos: Sequence[Sequence]):
        videos = (LibraryItem(*video) for video in videos)
        return cls(videos)

    def add(self, video: LibraryItem) -> None:
        self.__videos[video.get_id()] = video

    def remove(self, id: int) -> None:
        del self.__videos[id]

    def play(self):
        for item in self:
            item.increment_play_count()

    def __getitem__(self, video_id) -> LibraryItem:
        return self.__videos[video_id]

    def __iter__(self):
        return iter(self.__videos.values())

    def __contains__(self, id):
        return id in self.__videos

    def __bool__(self):
        return bool(self.__videos)
