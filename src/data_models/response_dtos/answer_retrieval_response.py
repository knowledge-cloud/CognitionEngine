from aws_lambda_powertools.utilities.parser import BaseModel

class AnswerRetrievalResponse(BaseModel):
    question: str
    answer: str