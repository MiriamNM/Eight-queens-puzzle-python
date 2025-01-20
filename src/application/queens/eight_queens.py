from result import Err, Ok
from domain.entities.queens.eight_queens import Queens
from domain.repositories.eight_queens_repository import EightQueensRepository


def queens_create(data, db_session) -> Ok | Err:
    try:
        n = getattr(data, 'n', 8)

        repository = EightQueensRepository(db_session)
        queens = repository.solve_n_queens(n, Queens)

        return Ok({
            "id": str(queens.id),
            "number_queens": queens.number_queens,
            "solutions": queens.solutions,
        })
    except Exception as e:
        return Err(f"Error creating queens")
