from pydantic import BaseModel, Field
from result import Err, Ok
from domain.entities.queens.eight_queens import Queens
from domain.repositories.eight_queens_repository import EightQueensRepository


class QueensInput(BaseModel):
    n: int = Field(default=8, ge=4, le=16)


def queens_create(data: QueensInput, db_session) -> Ok | Err:
    try:
        n = getattr(data, 'n', 8)

        repository = EightQueensRepository(db_session)
        result = repository.solve_n_queens(n, Queens)

        return Ok({
            "id": str(result.id),
            "number_queens": result.number_queens,
            "solutions": result.solutions,
        })
    except Exception as e:
        return Err(f"Error creating queens: {str(e)}")
