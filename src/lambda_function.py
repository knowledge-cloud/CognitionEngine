from typing import Dict
from data_models.enums import EventType
from services.retrieval_service import RetrievalServiceInstance
from data_models.response_dtos.lambda_response import LambdaResponse
from utils.log_utils import kclogger
from utils.log_utils import LogUtils
import time


def lambda_handler(event: Dict, context) -> LambdaResponse:
    start_time = time.time()
    kclogger.info(f"Cognition Engine Lambda Handler Called with {LogUtils.stringifier(event)}")    

    eventType = event["eventType"]
    if eventType is not None and eventType == EventType.RETRIEVAL.value:
        response = LambdaResponse(
            statusCode=200,
            body=RetrievalServiceInstance.getAnswer(event["data"])
        ).dict()
        kclogger.info(f"Cognition Engine Lambda Handler Returning {LogUtils.stringifier(response)}")
        kclogger.info(f"Cognition Engine Lambda Handler Took {time.time() - start_time} seconds")
        return response
    else:
        kclogger.info(f"Cognition Engine Lambda Handler Returning Invalid Event Type")
        kclogger.info(f"Cognition Engine Lambda Handler Took {time.time() - start_time} seconds")
        return LambdaResponse(
            statusCode=400,
            body=f"Invalid event type {event.eventType}"
        ).dict()