from venv import logger
from fastapi import HTTPException
from result import Err, Ok
from domain.entities.queens.eight_queens import Queens
from domain.repositories.eight_queens_repository import EightQueensRepository


def queens_create(data, db_session) -> dict:
    try:
        n = data.n if hasattr(data, 'n') else 8
        session = db_session
        print(n)

        if n < 1:
            raise HTTPException(
                status_code=400, detail="`n` must be greater than 0.")

        if not session:
            raise Exception("Database session not provided in context")

        repository = EightQueensRepository(session)
        queens = repository.solve_n_queens(n, Queens)

        return Ok({
            "id": queens.id,
            "number_queens": queens.number_queens,
            "solutions": queens.solutions,
        })
    except Exception as e:
        return Err(e)
