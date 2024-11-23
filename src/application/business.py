from domain.entities.example import EightQueensSolution
from domain.repositories.repository_example import ExampleRepository


def solve_puzzle() -> EightQueensSolution:
    # Ejemplo de lógica de negocio
    solution = ExampleRepository().generate_solution()
    return EightQueensSolution(positions=solution)
