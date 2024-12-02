from result import Err, Ok
from domain.entities.queens.eight_queens import Queens
from domain.repositories.eight_queens_repository import EightQueensRepository


def queens_create(data, context):
    try:
        n = data.get('n', 8)
        email = context.get('email')
        session = context.get('db_session')

        if not session:
            raise Exception("Database session not provided in context")

        repository = EightQueensRepository(session)
        queens = repository.solve_n_queens(n, email, Queens)

        return Ok({
            "id": queens.id,
            "number_queens": queens.number_queens,
            "solutions": queens.solutions,
            "created_by": queens.created_by,
        })
    except Exception as e:
        return Err(e)
