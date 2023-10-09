from models.request_dtos.question_retrieval_request import QuestionRetrievalRequest
from models.response_dtos.answer_retrieval_response import AnswerRetrievalResponse, AnswerRetrievalResponseBuilder
from utils.log_utils import kclogger


class RetrievalService:
    def getAnswer(self, request: QuestionRetrievalRequest) -> AnswerRetrievalResponse:
        kclogger.info(f"Retrieval Service Called with request: {request}")        
        data = AnswerRetrievalResponseBuilder(
            question=request.query,
            answer="Hello World"
        )
        return AnswerRetrievalResponse(
            status_code=200,
            body=data
        )
    
RetrievalServiceInstance = RetrievalService()