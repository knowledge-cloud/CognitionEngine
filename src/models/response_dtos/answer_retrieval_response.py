from aws_lambda_powertools.utilities.parser import BaseModel

class AnswerRetrievalResponseBuilder(BaseModel):
    query: str
    result: str


class AnswerRetrievalResponse(BaseModel):
    statusCode: int
    body: AnswerRetrievalResponseBuilder