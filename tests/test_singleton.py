import pytest
from app.singleton import SingletonMeta

def test_singleton():
    class TestObj(metaclass=SingletonMeta):
        pass
    class TestObj2(metaclass=SingletonMeta):
        pass
    assert TestObj() is TestObj()
    assert TestObj() is not TestObj2()
