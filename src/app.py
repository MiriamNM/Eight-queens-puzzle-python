from fastapi import FastAPI
from application.business import solve_puzzle
from domain.entities.example import EightQueensSolution

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Eight Queens Puzzle API"}


@app.post("/solve", response_model=EightQueensSolution)
def solve():
    return solve_puzzle()
