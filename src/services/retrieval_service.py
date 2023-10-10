from typing import Dict
from models.response_dtos.answer_retrieval_response import AnswerRetrievalResponse, AnswerRetrievalResponseBuilder
from models.request_dtos.question_retrieval_request import QuestionRetrievalRequest
from embeddings.generators.embedding_generator import EmbeddingSource, generate_embedding
from utils.log_utils import kclogger
from utils.log_utils import LogUtils
from storages.retrievers.storage_retrievers import query_from_storage, StorageSource


class RetrievalService:
    def getAnswer(self, request: Dict) -> AnswerRetrievalResponse:
        kclogger.info(f"RetrievalService::getAnswer called with request: {LogUtils.stringifier(request)}")       
        request = QuestionRetrievalRequest(**request)

        query = request.query
        query_embedding = generate_embedding(text=query, embedding_source=EmbeddingSource.OPENAI)
        nearest_nodes = query_from_storage(
            embedding=query_embedding, 
            top_k=1, 
            schema=request.schema, 
            storageSource=StorageSource.WEAVIATE
        )
        
        data = AnswerRetrievalResponseBuilder(
            query=request.query,
            result="Hello World"
        )
        return AnswerRetrievalResponse(
            statusCode=200,
            body=data
        )
    
RetrievalServiceInstance = RetrievalService()