import logging
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from application.business import business_logic

logger = logging.getLogger(__name__)
app = FastAPI()


class RequestModel(BaseModel):
    n: int
    context: dict


@app.get("/")
def read_root():
    return {"message": "Welcome to the Eight Queens Puzzle API"}


@app.post("/queens")
def solve(request: RequestModel):
    try:
        n = request.n
        context = request.context

        if n < 1:
            raise HTTPException(status_code=400, detail="`n` must be greater than 0.")

        logger.info(f"Processing request for n={n}")

        result = business_logic({"n": n}, context)

        return {"success": True, "result": result}
    except HTTPException as e:
        logger.error(f"HTTP error: {e.detail}")
        raise
    except Exception as e:
        logger.exception("Unexpected error occurred.")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")


@app.exception_handler(404)
async def not_found_handler(request: Request, exc):
    return JSONResponse(
        status_code=404,
        content={"message": "Endpoint not found"},
    )
