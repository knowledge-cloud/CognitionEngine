from aws_lambda_powertools.utilities.parser import BaseModel
from data_models.enums import EventType
from data_models.request_dtos.question_retrieval_request import QuestionRetrievalRequest


class CognitionEngineEvent(BaseModel):
    eventType: EventType
    data: QuestionRetrievalRequest
