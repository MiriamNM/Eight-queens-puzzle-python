import pytest
from unittest.mock import MagicMock
from uuid import uuid4
from domain.repositories.eight_queens_repository import EightQueensRepository
from domain.entities.queens.eight_queens import Queens


@pytest.fixture
def mock_db_session():
    """Fixture para simular la base de datos"""
    return MagicMock()


@pytest.fixture
def mock_queens():
    """Fixture para simular el objeto Queens"""
    mock_queens_instance = MagicMock(spec=Queens)
    mock_queens_instance.id = uuid4()
    mock_queens_instance.number_queens = 8
    mock_queens_instance.solutions = [
        '|_||♔||_||_|\\n|_||_||_||♔|\\n|♔||_||_||_|\\n|_||_||♔||_|',
        '|_||_||♔||_|\\n|♔||_||_||_|\\n|_||_||_||♔|\\n|_||♔||_||_|'
    ]
    return mock_queens_instance


def test_solve_n_queens(mock_db_session, mock_queens):
    repository = EightQueensRepository(mock_db_session)

    repository.solve_n_queens = MagicMock(return_value=mock_queens)

    n = 8
    queens_instance = repository.solve_n_queens(n, Queens)

    assert queens_instance == mock_queens
    assert queens_instance.number_queens == 8
    assert len(queens_instance.solutions) > 0


def test_solve_n_queens_commit(mock_db_session, mock_queens):
    repository = EightQueensRepository(mock_db_session)

    mock_db_session.add = MagicMock()
    mock_db_session.commit = MagicMock()
    mock_db_session.refresh = MagicMock()

    n = 8
    queens_instance = repository.solve_n_queens(n, Queens)

    mock_db_session.add.assert_called_once_with(queens_instance)
    mock_db_session.commit.assert_called_once()
    mock_db_session.refresh.assert_called_once_with(queens_instance)
