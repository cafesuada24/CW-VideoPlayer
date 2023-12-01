import pytest
from app.core.search_engine import HashMap, SearchEngine


class TestHashMap:
    def setup_method(self):
        self.hash_map = HashMap()

    def test_insert(self):
        self.hash_map.insert('test', 1)
        assert self.hash_map.search_prefix('test') == {1}

    def test_search_prefix(self):
        self.hash_map.insert('test', 1)
        self.hash_map.insert('test', 2)
        self.hash_map.insert('testing', 3)
        assert self.hash_map.search_prefix('test') == {1, 2, 3}


class TestSearchEngine:
    def setup_method(self):
        self.search_engine = SearchEngine(
            [('test', 1), ('test', 2), ('testing', 3)]
        )

    def test_search_prefix(self):
        assert self.search_engine.search_prefix('test') == {1, 2, 3}
