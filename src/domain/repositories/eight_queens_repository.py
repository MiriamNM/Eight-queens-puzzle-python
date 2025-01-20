from typing import List
from uuid import uuid4

from pydantic import BaseModel, Field
from result import Err

from domain.entities.queens.eight_queens import Queens


class QueensInput(BaseModel):
    n: int = Field(default=8, ge=4, le=16)


class EightQueensRepository:
    def __init__(self, session):
        self.session = session

    def solve_n_queens(self, n: int, queens: Queens) -> Queens:
        try:
            QueensInput(n=n)
        except Exception as e:
            return Err(f"Error en el número de las reinas: {str(e)}")

        results = []
        if n == 1 or n >= 4:
            self.recursive_function(results, [], n, 0)

        flat_results = ["\n".join(board) for board in results]

        queens_instance = Queens(
            id=uuid4(),
            number_queens=n,
            solutions=flat_results,
        )

        self.session.add(queens_instance)
        self.session.commit()
        self.session.refresh(queens_instance)
        return queens_instance

    def is_valid_position(self, result_arr: List[List[int]], position: List[int]) -> bool:
        for queen in result_arr:
            if queen[0] == position[0] or queen[1] == position[1]:
                return False
            if abs(queen[0] - position[0]) == abs(queen[1] - position[1]):
                return False
        return True

    def build_board(self, arr: List[List[int]], n: int) -> List[str]:
        board = []
        for i in range(n):
            row = ""
            for j in range(n):
                row += "|♔|" if [i, j] in arr else "|_|"
            board.append(row)
        return board

    def recursive_function(self, result_arr: List[List[int]], current_arr: List[List[int]], n: int, row: int):
        if row == n:
            result_arr.append(self.build_board(current_arr, n))
            return

        for col in range(n):
            if self.is_valid_position(current_arr, [row, col]):
                current_arr.append([row, col])

                self.recursive_function(result_arr, current_arr, n, row + 1)
                current_arr.pop()
