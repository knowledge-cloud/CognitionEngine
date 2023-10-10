from typing import Dict
from models.response_dtos.answer_retrieval_response import AnswerRetrievalResponse, AnswerRetrievalResponseBuilder
from models.request_dtos.question_retrieval_request import QuestionRetrievalRequest
from embeddings.generators.embedding_generator import EmbeddingSource, generate_embedding
from utils.log_utils import kclogger
from utils.log_utils import LogUtils
from storages.retrievers.storage_retrievers import query_from_storage, StorageSource
from response_synthesizers.summary_synthesizer import synthesize_summary


class RetrievalService:
    def getAnswer(self, request: Dict) -> AnswerRetrievalResponse:
        kclogger.info(f"RetrievalService::getAnswer called with request: {LogUtils.stringifier(request)}")       
        request = QuestionRetrievalRequest(**request)

        query = request.query
        query_embedding = generate_embedding(text=query, embedding_source=EmbeddingSource.OPENAI)
        query_result = query_from_storage(
            embedding=query_embedding, 
            top_k=1, 
            schema=request.knowledgeBaseIndex, 
            storageSource=StorageSource.WEAVIATE
        )
        
        text_chunks = [node.text for node in query_result.nodes]
        result = synthesize_summary(query=query, text_list=text_chunks)
        response_data = AnswerRetrievalResponseBuilder(
            query=query,
            result=result
        )
        return AnswerRetrievalResponse(
            statusCode=200,
            body=response_data
        )
    
RetrievalServiceInstance = RetrievalService()