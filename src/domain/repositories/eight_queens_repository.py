from typing import List
import pendulum
import uuid_extensions.uuid7 as uuid7
from domain.constants import TZ

from domain.entities.queens.eight_queens import Queens


class EightQueensRepository:
    def __init__(self, session):
        self.session = session

    def solve_n_queens(self, n: int, email: str, queens: Queens) -> Queens:
        results = []
        if n == 1 or n >= 4:
            self.recursive_function(results, [], n, 0)

        queens_instance = Queens(
            id=uuid7(),
            number_queens=n,
            solutions=results,
            created_by=email,
            created_at=pendulum.now("America/Mexico_City"),
        )

        self.session.add(queens_instance)
        self.session.commit()
        return queens_instance

    def is_valid_position(self, result_arr: List[List[int]], position: List[int]) -> bool:
        """
        Verifica si es seguro colocar una reina en la posición actual.
        - No debe haber otra reina en la misma fila o columna.
        - No debe haber otra reina en la misma diagonal.
        """
        for queen in result_arr:
            if queen[0] == position[0] or queen[1] == position[1]:
                return False
            if abs(queen[0] - position[0]) == abs(queen[1] - position[1]):
                return False
        return True

    def build_board(self, arr: List[List[int]], n: int) -> List[str]:
        """
        Construye una representación visual del tablero con las reinas.
        """
        board = []
        for i in range(n):
            row = ""
            for j in range(n):
                row += "|♔|" if [i, j] in arr else "|_|"
            board.append(row)
        return board

    def recursive_function(self, result_arr: List[List[int]], current_arr: List[List[int]], n: int, row: int):
        """
        Función recursiva que coloca las reinas fila por fila.
        """
        if row == n:  # Si todas las reinas están colocadas
            result_arr.append(self.build_board(current_arr, n))
            return

        for col in range(n):
            if self.is_valid_position(current_arr, [row, col]):
                current_arr.append([row, col])  # Coloca una reina
                # Avanza a la siguiente fila
                self.recursive_function(result_arr, current_arr, n, row + 1)
                current_arr.pop()  # Retrocede (backtracking)
