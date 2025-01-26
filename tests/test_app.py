import pytest
from unittest.mock import Mock
from sqlalchemy.orm import Session
from app import RequestModel, get_queens, solve
from utils.error_messages import ERRORS
from utils.success_messages import SUCCESS_MESSAGE


@pytest.fixture
def mock_db_session():
    return Mock(spec=Session)


def test_solve_valid_request(mock_db_session):
    request_data = RequestModel(n=8, context={})
    response = solve(request=request_data, db_session=mock_db_session)
    assert response["result"] == SUCCESS_MESSAGE.queens_are_kept
    assert response["error"] == ""


def test_solve_invalid_n(mock_db_session):
    with pytest.raises(ValueError):
        request_data = RequestModel(n=20, context={})
        solve(request=request_data, db_session=mock_db_session)


def test_get_queens_empty_database(mock_db_session):
    mock_db_session.query.return_value.all.return_value = []
    response = get_queens(db_session=mock_db_session)
    assert response["error"] == ERRORS.answers_are_not_found
    assert response["result"] is None
