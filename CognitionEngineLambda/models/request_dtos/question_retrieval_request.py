from aws_lambda_powertools.utilities.parser import BaseModel
from models.enums import KnowledgeBaseIndex


class QuestionRetrievalRequest(BaseModel):
    query: str
    knowledge_base_index: KnowledgeBaseIndex
