from typing import Dict

from data_models.request_dtos.question_retrieval_request import \
    QuestionRetrievalRequest
from data_models.response_dtos.answer_retrieval_response import \
    AnswerRetrievalResponse
from embeddings.generators.embedding_generator import (
    EmbeddingGeneratorInstance, EmbeddingSource)
from response_synthesizers.summary_synthesizer import \
    SummarySynthesizerInstance
from storages.retrievers.storage_retrievers import (StorageRetrieversInstance,
                                                    StorageSource)
from utils.log_utils import LogUtils, kclogger


class RetrievalService:
    def getAnswer(self, request: QuestionRetrievalRequest) -> AnswerRetrievalResponse:
        kclogger.info(
            f"RetrievalService::getAnswer::request: {LogUtils.stringifier(request)}")

        query_embedding = EmbeddingGeneratorInstance.generate_embedding(
            text=request.query, embedding_source=EmbeddingSource.OPENAI)

        query_result = StorageRetrieversInstance.query(
            embedding=query_embedding,
            top_k=1,
            knowledge_base=request.knowledgeBaseIndex,
            storage_source=StorageSource.WEAVIATE
        )

        text_chunks = [doc.page_content for doc in query_result]
        result = SummarySynthesizerInstance.synthesize_summary(
            query=request.query, text_list=text_chunks)

        return AnswerRetrievalResponse(
            question=request.query,
            answer=result
        )


RetrievalServiceInstance = RetrievalService()
