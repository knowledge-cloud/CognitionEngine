from enum import Enum
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
            top_k: int, schema: str, 
            storageSource: StorageSource
    ) -> VectorStoreQueryResult:
        if storageSource == StorageSource.WEAVIATE:
            self.weaviate_storage.query(embedding, top_k, schema)
        else:
            raise StorageRetrieversError("Invalid storage source")

StorageRetrieversInstance = StorageRetrievers()
query_from_storage = StorageRetrieversInstance.query_from_storage
