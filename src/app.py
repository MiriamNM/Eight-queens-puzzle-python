import logging
from pydantic import BaseModel
from infrastructure.flyway_manager import run_flyway_migrations, check_flyway_status

from result import Err
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from application.business import business_logic

logger = logging.getLogger(__name__)
app = FastAPI()


class RequestModel(BaseModel):
    n: int
    context: dict


@app.get("/version")
async def get_version():
    return {"version": "1.0.0"}


@app.get("/")
def read_root():
    return {"message": "Welcome to the Eight Queens Puzzle API"}


@app.post("/queens")
def solve(request: RequestModel):
    try:
        n = request.n
        context = request.context

        if not isinstance(context, dict):
            logger.error("Invalid context value.")
            return Err("Invalid context value.")

        return business_logic({"n": n}, context)
    except Exception as e:
        return Err(str(e))


@app.exception_handler(404)
async def not_found_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={"message": "Endpoint not found"},
    )

def main():
    # Verificar el estado de las migraciones
    check_flyway_status()

    # Ejecutar las migraciones
    run_flyway_migrations()

if __name__ == "__main__":
    main()
