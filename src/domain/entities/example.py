from pydantic import BaseModel
from typing import List


class EightQueensSolution(BaseModel):
    positions: List[List[int]]
