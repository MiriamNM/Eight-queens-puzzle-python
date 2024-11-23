from application.business import solve_puzzle


def test_solve_puzzle():
    solution = solve_puzzle()
    assert len(solution.positions) == 8
    for row in solution.positions:
        assert sum(row) == 1
