import logging
from result import Ok, Err

from application.queens.eight_queens import queens_create

logger = logging.getLogger(__name__)


uses_cases = {
    "queens-puzzle-create": queens_create,
}


def business_logic(data, context) -> dict:
    logger.info(f"context: {context}")
    logger.info(f"Data: {data}")

    event = context.get("event")

    if not event:
        raise Exception("No event found in context")

    if event not in uses_cases:
        raise Exception(f"Event {event} not found")

    use_case = uses_cases[event]
    result = use_case(data, context)

    match result:
        case Ok(value):
            return {
                "response": value,
                "error": ""
            }
        case Err(error):
            return {
                "response": "",
                "error": str(error)
            }
