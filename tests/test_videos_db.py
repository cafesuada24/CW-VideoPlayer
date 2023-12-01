import pytest
from app.core.video_library import VideosDB
from app.namespaces.queries import Queries


class TestVideosDB:
    db = VideosDB()

    def test_connection(self):
        assert self.db.cursor is not None

    def test_update(self):
        pass
