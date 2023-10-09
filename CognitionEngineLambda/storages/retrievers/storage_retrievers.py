from enum import Enum
from storages.retrievers.weaviate_storage_retrievers import WeaviateStorageRetriever

class StorageRetrieversError(Exception):
    pass

class StorageSource(Enum):
    WEAVIATE = "WEAVIATE"


class StorageRetrievers:
    def __init__(self):
        self.weaviate_storage = WeaviateStorageRetriever()

    def queryFromStorage(self, embedding: list[float], top_k: int, schema: str, storageSource: StorageSource):
        if storageSource == StorageSource.WEAVIATE:
            self.weaviate_storage.query(embedding, top_k, schema)
        else:
            raise StorageRetrieversError("Invalid storage source")
