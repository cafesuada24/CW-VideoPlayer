import sqlite3
from pathlib import Path
from unittest import mock

import pytest
from app.core.videos_db import VideosDB
from app.namespaces.queries import Queries
from app import CONFIG


class TestVideosDB:
    @classmethod
    def setup_class(cls):
        db_path = Path(CONFIG['database']['path']['db'])
        if db_path.exists():
            db_path.unlink()
        cls.db = VideosDB()

    def test_connection(self):
        assert self.db.cursor is not None

    def test_getall(self):
        all_data = self.db.get_all()
        assert isinstance(all_data, tuple)
        assert bool(all_data)

    def test_close(self):
        self.db.close()
        with pytest.raises(sqlite3.ProgrammingError):
            self.db.cursor.execute(
                Queries.SELECT_ALL.safe_substitute(table=self.db.TABLE)
            )
