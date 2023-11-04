from pathlib import Path
from typing import NamedTuple
import sqlite3 as sql

class VideosDB:
    def __init__(self, path=None):
        self.__db_file = Path(path or self.DEFAULT_DB_PATH)
        self.__conn = None
        self.__cursor = None
    
    @property
    def ROOT_FOLDER(self):
        return __file__.rsplit('/', 2)[0]
    
    @property
    def DEFAULT_DB_PATH(self):
        return self.ROOT_FOLDER + "/data/videos.db"
    
    @property
    def TABLE_NAME(self):
        return 'videos'
    
    @property
    def SCHEMA(self):
        return self.ROOT_FOLDER + '/docs/dbschema.sql'

    def __ensure_table(self):
        if self.__cursor is None: return
        
        query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.TABLE_NAME}'"
        self.__cursor.execute(query)

        if self.__cursor.fetchone() is not None:
            return

        with open(self.SCHEMA, 'r') as f:
            self.__cursor.executescript(f.read())

    def __enter__(self):
        self.__conn = sql.connect(self.__db_file)
        self.__cursor = self.__conn.cursor()
        self.__ensure_table()
        return self.__cursor

    def __exit__(self, exec_tp, exec_val, exec_tb):
        self.__conn.commit()
        self.__cursor.close()
        self.__conn.close()

class UpdateTransaction(NamedTuple):
    column: str
    value: str
    id: int
