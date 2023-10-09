from aws_lambda_powertools.utilities.parser import event_parser
from models.enums import EventType
from models.events.cognition_engine_event import CognitionEngineEvent
from services.retrieval_service import RetrievalServiceInstance
from models.response_dtos.lambda_response import LambdaResponse
from utils.log_utils import kclogger

@event_parser(model=CognitionEngineEvent)
def lambda_handler(event: CognitionEngineEvent, context) -> dict:
    kclogger.info(f"Cognition Engine Lambda Handler Called with event {event}")

    if event.eventType == EventType.RETRIEVAL.value:
        answerResponse = RetrievalServiceInstance.getAnswer(event.data)
        response = LambdaResponse(
            status_code=200,
            body=answerResponse.__dict__
        )
        kclogger.info(f"Cognition Engine Lambda Handler Returning {response}")
        return response.__dict__
    else:
        return LambdaResponse(
            status_code=400,
            body=f"Invalid event type {event.eventType}"
        ).__dict__