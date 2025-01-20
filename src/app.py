import logging
from sre_constants import SUCCESS
from typing import Optional
from pydantic import BaseModel, Field
from fastapi import Depends, FastAPI
from result import Ok, Err
from sqlalchemy.orm import Session
from application.queens.eight_queens import queens_create
from domain.entities.queens.eight_queens import Queens
from infrastructure.entity_manager import get_db_session
from utils.error_messages import ERRORS
from utils.serealize_queen import serialize_queen

logger = logging.getLogger(__name__)

app = FastAPI()


class RequestModel(BaseModel):
    n: int = Field(default=8, ge=4, le=16)
    context: dict


class ResponseModel(BaseModel):
    result: Optional[str] = None
    error: Optional[str] = None


@app.post("/queens/", response_model=ResponseModel)
def solve(request: RequestModel, db_session: Session = Depends(get_db_session)):
    try:
        response = queens_create(request, db_session)
        return {"result": SUCCESS.queens_are_kept, "error": ""}
    except Exception as e:
        print(f"Error in solve: {e}")
        return {"result": "", "error": ERRORS.cloud_not_created}


@app.get("/queens/", response_model=ResponseModel)
def get_queens(db_session: Session = Depends(get_db_session)):
    try:
        queens_list = db_session.query(Queens).all()
        if not queens_list:
            return {"error": ERRORS.answers_are_not_found, "result": None}

        result = [serialize_queen(queen) for queen in queens_list]
        return {"result": str(result), "error": None}
    except Exception as e:
        return {"result": None, "error": ERRORS.cannot_view_saved}
