import pytest
from unittest.mock import patch
from app.core.video_library import LibraryItem, LibraryItemCollection
from app.core.videos_db import VideosDB


class TestLibraryItem:
    item = LibraryItem(1, 'Video1', 'Director', 3, 1, '/abc/def.mp4')

    def test_list_all(self):
        assert self.item.list_all((0, 1, 2)) == (1, 'Video1', 'Director')
        assert self.item.list_all(('file_path', 'video_id', 'play_count')) == (
            '/abc/def.mp4',
            1,
            1,
        )
        assert self.item.list_all() == (
            1,
            'Video1',
            'Director',
            3,
            1,
            '/abc/def.mp4',
        )

    def test_init_value(self):
        assert self.item.get_id() == 1
        assert self.item.get_name() == 'Video1'
        assert self.item.get_director() == 'Director'
        assert self.item.get_rating() == 3
        assert self.item.get_play_count() == 1
        assert self.item.get_file_path() == '/abc/def.mp4'

    def test_index_subscription(self):
        assert self.item.get_id() == self.item[0]
        assert self.item.get_name() == self.item[1]
        assert self.item.get_director() == self.item[2]
        assert self.item.get_rating() == self.item[3]
        assert self.item.get_play_count() == self.item[4]
        assert self.item.get_file_path() == self.item[5]

    def test_update_methods(self):
        with patch('app.core.videos_db.VideosDB.update', return_value=None):
            self.item.increment_play_count()
            assert self.item.get_play_count() == 2

            self.item.set_name('videoblah')
            assert self.item.get_name() == 'videoblah'

            self.item.set_director('Directorbuh')
            assert self.item.get_director() == 'Directorbuh'

            self.item.set_rating('4')
            assert self.item.get_rating() == 4

            self.item.set_file_path('new/path')
            assert self.item.get_file_path() == 'new/path'

    def test_update_methods_using_index_supscription(self):
        with patch('app.core.videos_db.VideosDB.update', return_value=None):
            self.item[4] += 1
            assert self.item.get_play_count() == 3

            self.item[1] = 'aha'
            assert self.item.get_name() == 'aha'

            self.item[2] = 'lmao'
            assert self.item.get_director() == 'lmao'

            self.item[3] = 5
            assert self.item.get_rating() == 5

            self.item[5] = 'another/path'
            assert self.item.get_file_path() == 'another/path'


class TestLibraryItemCollection:
    item1 = LibraryItem(1, 'Video1', 'Director', 3, 1, '/abc/def.mp4')
    item2 = LibraryItem(2, 'Video2', 'Dir', 2, 3, 'abc/egh.mp4')

    collection = LibraryItemCollection((item1,))

    def test_membership(self):
        assert 1 in self.collection
        assert 2 not in self.collection
        assert 0 not in self.collection

    def test_add(self):
        self.collection.add(self.item2)
        assert 1 in self.collection
        assert 2 in self.collection

    def test_remove(self):
        self.collection.remove(1)
        assert 1 not in self.collection
        assert 2 in self.collection

    def test_getitem(self):
        assert self.collection[2] == self.item2

    def test_values(self):
        assert tuple(self.collection.values()) == (self.item2,)

    def test_iter(self):
        for item in self.collection:
            assert item == self.item2
