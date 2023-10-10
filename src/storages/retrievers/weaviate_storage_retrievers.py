from weaviate import client as weaviate_client
from weaviate import AuthApiKey
from llama_index.vector_stores import WeaviateVectorStore
from llama_index.vector_stores.types import VectorStoreQuery, VectorStoreQueryResult

class WeaviateStorageRetriever: 
    def __init__(self):
        auth_config = AuthApiKey(api_key="WEAVIATE_API_KEY")
        self.weaviate_client = weaviate_client(self.url, auth_config)

    def query(self, embedding: list[float], top_k: int, schema: str) -> VectorStoreQueryResult:
        weaviate_store = WeaviateVectorStore(self.weaviate_client, schema)
        store_query = VectorStoreQuery(query_embedding=embedding, similarity_top_k=top_k, mode="default")
        return weaviate_store.query(store_query)