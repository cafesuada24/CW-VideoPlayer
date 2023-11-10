from collections import deque
from unittest.mock import Mock, patch

from app.core.videos_db import UpdateTransaction, VideosDB

class TestDB:
    def test_update(self):
        with patch.object(VideosDB, '__del__', return_value=None) as db:
            mock_transaction = Mock(spec=UpdateTransaction)
            db._VideosDB__transactions = deque()
            with patch('app.core.videos_db.UpdateTransaction',
                       return_value=mock_transaction):
                db.update(1, 'col', 'val')
                assert db._VideosDB__transactions == deque([mock_transaction])
                mock_transaction.assert_called_once_with(1, 'col', 'val')
       
