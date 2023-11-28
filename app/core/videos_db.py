import sqlite3 as sql
from pathlib import Path

from ..namespaces.queries import Queries
from ..singleton import SingletonMeta
from .. import CONFIG

CONFIG = CONFIG['database']


class VideosDB(metaclass=SingletonMeta):
    COLUMNS = (
        'video_id',
        'name',
        'director',
        'rating',
        'play_count',
        'file_path',
    )

    TABLE = 'videos'

    def __init__(self):
        db_path = Path(CONFIG['path']['db'])
        if not db_path.exists():
            db_path.parent.mkdir(parents=True, exist_ok=True)
            db_path.touch()
        self.__conn = sql.connect(db_path)
        self.__cursor = self.__conn.cursor()
        self.__ensure_db()

    @property
    def cursor(self):
        return self.__cursor

    def close(self):
        self.__conn.commit()
        self.cursor.close()
        self.__conn.close()

    def update(self, id: int, column: str, val: str | int) -> None:
        try:
            self.cursor.execute(
                Queries.UPDATE.safe_substitute(
                    table=self.TABLE, column=column, filter_col='video_id'
                ),
                (val, id),
            )
        except sql.OperationalError as e:
            print(e)

    def get_all(self) -> tuple:
        ret = None
        try:
            self.cursor.execute(
                Queries.SELECT_ALL.safe_substitute(table=self.TABLE)
            )
            ret = tuple(self.cursor.fetchall())
        except sql.OperationalError as e:
            print(e)
        return ret

    def __ensure_db(self):
        if self.__cursor is None:
            return

        self.__cursor.execute(Queries.SELECT_TABLE, (self.TABLE,))

        if self.__cursor.fetchone() is not None:
            return

        with open(CONFIG['path']['schema'], 'r') as f:
            self.cursor.executescript(f.read())
