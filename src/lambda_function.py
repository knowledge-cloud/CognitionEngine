import time
from typing import Dict

from data_models.enums import EventType
from data_models.request_dtos.question_retrieval_request import \
    QuestionRetrievalRequest
from data_models.response_dtos.lambda_response import LambdaResponse
from services.retrieval_service import RetrievalServiceInstance
from utils.log_utils import LogUtils, kclogger


def lambda_handler(event: Dict, context) -> LambdaResponse:
    start_time = time.time()
    kclogger.info(
        f"Cognition Engine Lambda Handler Called with {LogUtils.stringifier(event)}")

    eventType = event.get("eventType")
    match eventType:
        case EventType.RETRIEVAL.value:
            retrieval_request = QuestionRetrievalRequest(event["data"])
            response = LambdaResponse(
                statusCode=200,
                body=RetrievalServiceInstance.getAnswer(retrieval_request)
            ).model_dump()
            kclogger.info(
                f"[{time.time() - start_time} s]Cognition Engine Lambda Handler {LogUtils.stringifier(response)}")
            return response
        case default:
            kclogger.error(
                f"[{time.time() - start_time} s]Cognition Engine Lambda Handler Returning Invalid Event Type")
            return LambdaResponse(
                statusCode=400,
                body=f"Invalid event type {event.eventType}"
            ).model_dump()
