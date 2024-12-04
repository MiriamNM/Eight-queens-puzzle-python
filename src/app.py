import logging
from pydantic import BaseModel
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy import text
from application.business import business_logic
from domain.entities.queens.eight_queens import Queens
from infrastructure.entity_manager import get_db_session

logger = logging.getLogger(__name__)
app = FastAPI()


class RequestModel(BaseModel):
    n: int
    context: dict


class ResponseModel(BaseModel):
    success: bool
    result: dict
    error: str


@app.get("/")
def read_root():
    return {"message": "Welcome to the Eight Queens Puzzle API"}


@app.post("/queens/", response_model=ResponseModel)
def solve(request: RequestModel, db_session=Depends(get_db_session)):
    try:
        n = request.n
        context = request.context

        if n < 1:
            raise HTTPException(
                status_code=400, detail="`n` must be greater than 0.")

        context["db_session"] = db_session
        result = business_logic({"n": n}, context)

        return {"success": True, "result": result["response"], "error": ""}
    except HTTPException as e:
        logger.error(f"HTTP error: {e.detail}")
        raise
    except Exception as e:
        logger.exception("Unexpected error occurred.")
        raise HTTPException(
            status_code=500, detail="An unexpected error occurred.")


@app.get("/queens/")
def get_queens(db_session=Depends(get_db_session)):
    try:
        query = "SELECT * FROM queens"
        result = db_session.execute(text(query)).fetchall()

        if not result:
            return {"success": True, "result": [], "error": ""}

        queens_list = [dict(row._mapping) for row in result]

        return {"success": True, "result": queens_list, "error": ""}
    except Exception as e:
        logger.exception("Error al obtener las reinas desde la base de datos.")
        raise HTTPException(
            status_code=500, detail="Error al obtener los elementos de la tabla `queens`.")


@app.get("/users/")
def get_users(db=Depends(get_db_session)):
    try:
        result = db.query(queens_list).all()
        queens_list = [dict(row) for row in result]
        return result
    except Exception as e:
        logger.exception("Error al obtener las reinas desde la base de datos.")
        raise HTTPException(
            status_code=500, detail="Error al obtener los elementos de la tabla `queens`.")


@app.exception_handler(404)
async def not_found_handler(request: Request, exc):
    return JSONResponse(
        status_code=404,
        content={"message": "Endpoint not found"},
    )
