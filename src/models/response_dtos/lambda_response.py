from __future__ import annotations
from typing import Union
from aws_lambda_powertools.utilities.parser import BaseModel
from models.response_dtos.answer_retrieval_response import AnswerRetrievalResponse

class LambdaResponse(BaseModel):
    statusCode: int
    body: Union[AnswerRetrievalResponse, str]

