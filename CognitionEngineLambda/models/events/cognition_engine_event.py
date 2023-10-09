from aws_lambda_powertools.utilities.parser import BaseModel
from models.enums import EventType
from CognitionEngineLambda.models.request_dtos.question_retrieval_request import QuestionRetrievalRequest


class CognitionEngineEvent(BaseModel):
    eventType: EventType
    data: QuestionRetrievalRequest
