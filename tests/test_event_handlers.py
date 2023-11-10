import pytest
from unittest.mock import Mock

from app.events.event_handlers import EventHandler

class TestCheckVideo:
    @pytest.fixture(params=['valid', 'invalid1', 'invalid2'])
    def generate_tests(self, request):
        input = Mock()
        input.id = 1
        input.videos = {
                1: Mock(list_all=Mock(return_value=['A', 'B', 1, 1]))
                }
        input.output = Mock()
        output = "Name: A\nDirector: B\nRating: 1\nPlay Count: 1"

        if (request.param == 'invalid1'):
            input.id = 0
            output = 'Video number not found: 0'

        if (request.param == 'invalid2'):
            input.id = 'a'
            output = 'Video number not found: a'

        return input, output

    def test_check_video(self, generate_tests):
        event = generate_tests[0]
        expected = generate_tests[1]

        EventHandler.check_video(event)(Mock())
        
        event.output.assert_called_once_with(expected)

# class TestUpdateVideo:
#     @pytest.fixture(params=[])
#     def generate_tests(self):
#         pass
