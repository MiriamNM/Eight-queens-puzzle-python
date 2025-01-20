import uuid
import pytest
from unittest.mock import MagicMock, Mock
from sqlalchemy.orm import Session

from app import RequestModel, get_queens, solve

# Mock de la sesión de la base de datos


@pytest.fixture
def mock_db_session():
    return Mock(spec=Session)


def test_solve_valid_request(mock_db_session):
    # Crear un request válido
    request_data = RequestModel(n=8, context={})
    response = solve(request=request_data, db_session=mock_db_session)
    assert response["success"] is True
    assert response["result"] == "Se guardaron las reinas"
    assert response["error"] == ""


def test_solve_invalid_n(mock_db_session):
    # Crear un request con un valor inválido de `n`
    with pytest.raises(ValueError):
        request_data = RequestModel(n=11, context={})
        solve(request=request_data, db_session=mock_db_session)


def test_get_queens_empty_database(mock_db_session):
    # Simular una base de datos vacía
    mock_db_session.query.return_value.all.return_value = []
    response = get_queens(db_session=mock_db_session)
    assert response["error"] == "No se encontraron soluciones almacenadas."
    assert response["result"] is None
