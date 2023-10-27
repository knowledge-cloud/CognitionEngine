from enum import Enum
from typing import List

from langchain.schema.document import Document

from data_models.enums import KnowledgeBaseIndex
from storages.retrievers.weaviate_storage_retrievers import \
    WeaviateStorageRetriever
from utils.log_utils import kclogger


class StorageSource(Enum):
    WEAVIATE = "WEAVIATE"


class StorageRetrievers:
    class StorageRetrieversException(Exception):
        pass

    def query(
            self,
            embedding: list[float],
            top_k: int,
            knowledge_base: KnowledgeBaseIndex,
            storage_source: StorageSource
    ) -> List[Document]:
        match storage_source:
            case StorageSource.WEAVIATE:
                result = self.query_from_weaviate(
                    embedding=embedding, top_k=top_k, schema=knowledge_base.value)
                return result
            case default:
                kclogger.exception(f"Invalid storage source: {storage_source}")
                raise self.StorageRetrieversException(
                    f"Invalid storage source: {storage_source}")

    def query_from_weaviate(self, embedding: list[float], top_k: int, schema: str) -> List[Document]:
        weaviate_storage = WeaviateStorageRetriever()
        kclogger.info(
            f"StorageRetrievers::WEAVIATE: Schema: {schema}")
        result = weaviate_storage.query(
            embedding=embedding, top_k=top_k, schema=schema)
        kclogger.info(
            f"StorageRetrievers::WEAVIATE: Fetched total of {len(result)} results")
        return result


StorageRetrieversInstance = StorageRetrievers()
