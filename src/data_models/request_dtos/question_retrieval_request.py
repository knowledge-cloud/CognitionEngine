from aws_lambda_powertools.utilities.parser import BaseModel

from data_models.enums import KnowledgeBaseIndex


class QuestionRetrievalRequest(BaseModel):
    query: str
    knowledgeBaseIndex: KnowledgeBaseIndex
