import logging
from typing import Dict, List
from pydantic import BaseModel
from fastapi import Depends, FastAPI, HTTPException
from result import Ok
from sqlalchemy.orm import Session
from application.queens.eight_queens import queens_create
from domain.entities.queens.eight_queens import Queens
from infrastructure.entity_manager import get_db_session
from utils.serealize_queen import serialize_queen

logger = logging.getLogger(__name__)

app = FastAPI()


class RequestModel(BaseModel):
    n: int
    context: dict


class ResponseModel(BaseModel):
    result: str
    error: str


@app.get("/")
def read_root():
    return {"message": "Welcome to the Eight Queens Puzzle API"}


@app.post("/queens/", response_model=ResponseModel)
def solve(request: RequestModel, db_session: Session = Depends(get_db_session)):
    try:
        response = queens_create(request, db_session)
        if isinstance(response, Ok):
            return {"success": True, "result": "Se guardaron las reinas", "error": ""}
        else:
            raise HTTPException(status_code=500, detail=str(response.value))
    except Exception as e:
        logger.exception("Unexpected error occurred.")
        raise HTTPException(
            status_code=500, detail="An unexpected error occurred.")


@app.get("/queens/", response_model=ResponseModel)
def get_queens(db_session: Session = Depends(get_db_session)):
    try:
        queens_list = db_session.query(Queens).all()

        result = ""
        result = [serialize_queen(queen) for queen in queens_list]
        return {"success": True, "result": str(result), "error": ""}
    except Exception as e:
        logger.exception("Error al obtener las reinas desde la base de datos.")
        raise HTTPException(
            status_code=500, detail="Error al obtener los elementos de la tabla `queens`."
        )
