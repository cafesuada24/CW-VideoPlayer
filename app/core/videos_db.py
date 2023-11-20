import sqlite3 as sql
from collections import deque
from pathlib import Path
from typing import NamedTuple

from .. import CONFIG

CONFIG = CONFIG['database']

class VideosDB:
    def __init__(self):
        self.__db_file = CONFIG['path']['db']
        self.__transactions = deque() 
        self.__se = None
        self.__data = tuple

    def update(self, id: int, column: str, val: str | int) -> None:
        transaction = UpdateTransaction(id, column, val)
        self.__transactions.append(transaction)
    
    def get_all(self):
        query = f"SELECT * FROM {CONFIG['table']}"
        with self:
            self.__cursor.execute(query)
            ret = tuple(self.__cursor.fetchall())
        return tuple(ret)

    def __push_transactions(self):
        if not self.__transactions: return
        
        with self as cursor:
            while self.__transactions:
                tsx = self.__transactions.popleft()
                query = f'''
                UPDATE {CONFIG['table']}
                SET {tsx.column} = ?
                WHERE video_id = ?
                '''
                cursor.execute(query, (tsx.value, tsx.id))

    def __ensure_table(self):
        if self.__cursor is None: return
        
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name = ?"
        self.__cursor.execute(query, (CONFIG['table'],))

        if self.__cursor.fetchone() is not None:
            return

        with open(CONFIG['path']['schema'], 'r') as f:
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
    
    def __del__(self):
       self.__push_transactions() 

class UpdateTransaction(NamedTuple):
    id: int
    column: str
    value: str | int
