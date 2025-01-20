import pytest
from unittest.mock import MagicMock, patch
from infrastructure.entity_manager import get_db_session


@pytest.fixture
def mock_session():
    mock_session = MagicMock()
    yield mock_session
    mock_session.close.assert_called_once()


def test_get_db_session(mock_session):
    with patch('infrastructure.entity_manager.SessionLocal', return_value=mock_session):
        session = next(get_db_session())
        assert session == mock_session
        mock_session.close.assert_called_once()
