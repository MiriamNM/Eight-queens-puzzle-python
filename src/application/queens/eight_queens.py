# actions/eight_queens.py
from domain.entities.queens.eight_queens import Queens
from domain.repositories.eight_queens_repository import EightQueensRepository
from result import Err, Ok

from infrastructure.entity_manager import get_db_session


def queens_create(data, context):
    try:
        n = data.get('n', 8)
        email = context.get('email')

        session = next(get_db_session())

        repository = EightQueensRepository(session)
        queens = repository.solve_n_queens(n, email, Queens)

        result = Ok(queens)

        response = result.json()

        return response
    except Exception as e:
        return Err(e)
