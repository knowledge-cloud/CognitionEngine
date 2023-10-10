from typing import Dict
from models.enums import EventType
from services.retrieval_service import RetrievalServiceInstance
from models.response_dtos.lambda_response import LambdaResponse
from utils.log_utils import kclogger
from utils.log_utils import LogUtils

def lambda_handler(event: Dict, context) -> LambdaResponse:
    kclogger.info(f"Cognition Engine Lambda Handler Called with {LogUtils.stringifier(event)}")        

    eventType = event["eventType"]
    if eventType is not None and eventType == EventType.RETRIEVAL.value:
        response = LambdaResponse(
            statusCode=200,
            body=RetrievalServiceInstance.getAnswer(event["data"])
        ).dict()
        kclogger.info(f"Cognition Engine Lambda Handler Returning {LogUtils.stringifier(response)}")
        return response
    else:
        kclogger.info(f"Cognition Engine Lambda Handler Returning Invalid Event Type")
        return LambdaResponse(
            statusCode=400,
            body=f"Invalid event type {event.eventType}"
        ).dict()