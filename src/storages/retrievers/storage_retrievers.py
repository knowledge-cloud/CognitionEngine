from enum import Enum
from data_models.enums import KnowledgeBaseIndex
from utils.log_utils import kclogger
from storages.retrievers.weaviate_storage_retrievers import WeaviateStorageRetriever
from llama_index.vector_stores.types import VectorStoreQueryResult


class StorageRetrieversError(Exception):
    pass

class StorageSource(Enum):
    WEAVIATE = "WEAVIATE"


class StorageRetrievers:
    def __init__(self):
        self.weaviate_storage = WeaviateStorageRetriever()

    def query_from_storage(
            self, 
            embedding: list[float], 
            top_k: int, 
            schema: KnowledgeBaseIndex, 
            storageSource: StorageSource
    ) -> VectorStoreQueryResult:
        kclogger.info(f"StorageRetrievers::query_from_storage called with schema: {schema} and storageSource: {storageSource}")
        if storageSource == StorageSource.WEAVIATE:
            # TODO - remove this hardcoding of schema
            result = self.weaviate_storage.query(embedding=embedding, top_k=top_k, schema="KCIndex")
            kclogger.info(f"StorageRetrievers::query_from_storage fetched total of {len(result.nodes)} results")
            return result
        else:
            raise StorageRetrieversError("Invalid storage source")

StorageRetrieversInstance = StorageRetrievers()
query_from_storage = StorageRetrieversInstance.query_from_storage
