import weaviate
from weaviate import AuthApiKey
from llama_index.vector_stores import WeaviateVectorStore
from llama_index.vector_stores.types import VectorStoreQuery, VectorStoreQueryResult
import os

class WeaviateStorageRetriever: 
    def __init__(self):
        url = os.environ.get('WEAVIATE_URL')
        weaviate_key = os.environ.get('WEAVIATE_API_KEY')
        auth_config = AuthApiKey(api_key=weaviate_key)
        self.weaviate_client = weaviate.Client(url, auth_client_secret=auth_config)

    def query(self, embedding: list[float], top_k: int, schema: str) -> VectorStoreQueryResult:
        weaviate_store = WeaviateVectorStore(weaviate_client=self.weaviate_client, index_name=schema)
        store_query = VectorStoreQuery(query_embedding=embedding, similarity_top_k=top_k, mode="default")
        return weaviate_store.query(store_query)