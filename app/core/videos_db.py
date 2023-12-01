"""This module contains Database connection class"""

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
    )  # all columns in database

    TABLE = 'videos'

    def __init__(self, db_path=None):
        db_path = db_path or Path(
            CONFIG['path']['db']
        )  # get database path from config
        if not db_path.exists():
            db_path.parent.mkdir(parents=True, exist_ok=True)
            db_path.touch()
        self.__conn = sql.connect(db_path)  # Create database connection
        self.__cursor = self.__conn.cursor()  # fetch database cursor
        self.__ensure_db()  # makesure database exists

    @property
    def cursor(self):
        return self.__cursor

    def close(self):
        """Close database connection"""

        self.__conn.commit()
        self.cursor.close()
        self.__conn.close()

    def update(self, id: int, column: str, val: str | int) -> None:
        """Update database data
        Args:
            id - video_id
            column - column to update
            val - new value
        """
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
        """Return database data"""

        ret = None
        try:
            self.__conn.commit()
            self.cursor.execute(
                Queries.SELECT_ALL.safe_substitute(table=self.TABLE)
            )
            ret = tuple(self.cursor.fetchall())
        except sql.OperationalError as e:
            print(e)
        return ret

    def __ensure_db(self):
        """Makesure database exists"""

        if self.__cursor is None:
            # if there is no cursor
            return

        # Check table existance
        self.__cursor.execute(Queries.SELECT_TABLE, (self.TABLE,))

        if self.__cursor.fetchone() is not None:
            # If the table exists
            return

        with open(CONFIG['path']['schema'], 'r') as f:
            # Init database by database schema
            self.cursor.executescript(f.read())
