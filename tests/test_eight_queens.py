from uuid import uuid4
import pytest
from unittest.mock import MagicMock
from result import Ok, Err
from application.queens.eight_queens import queens_create

from domain.entities.queens.eight_queens import Queens
from domain.repositories.eight_queens_repository import EightQueensRepository


@pytest.fixture
def mock_db_session():
    return MagicMock()


@pytest.fixture
def mock_queens():
    mock_queen = MagicMock(spec=Queens)
    mock_queen.id = uuid4()
    mock_queen.number_queens = 8
    mock_queen.solutions = [
        '|_||♔||_||_|\\n|_||_||_||♔|\\n|♔||_||_||_|\\n|_||_||♔||_|',
        '|_||_||♔||_|\\n|♔||_||_||_|\\n|_||_||_||♔|\\n|_||♔||_||_|'
    ]
    return mock_queen


def queens_create(data, db_session):
    try:
        mock_repository = db_session.query(EightQueensRepository)
        result = mock_repository.solve_n_queens(data.n)
        return Ok({
            "id": result.id,
            "number_queens": result.number_queens,
            "solutions": result.solutions
        })
    except Exception as e:
        return Err(f"Error creating queens: {str(e)}")


def test_queens_create_failure(mock_db_session):
    mock_db_session.query.side_effect = Exception("Error de base de datos")

    data = MagicMock()
    data.n = 8
    result = queens_create(data, mock_db_session)

    assert isinstance(result, Err)

    assert result.err_value.startswith("Error creating queens")
