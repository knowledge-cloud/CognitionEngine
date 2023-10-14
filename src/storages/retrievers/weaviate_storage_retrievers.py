from utils.log_utils import kclogger
import weaviate
from weaviate import AuthApiKey
from llama_index.vector_stores import WeaviateVectorStore
from llama_index.vector_stores.types import VectorStoreQuery, VectorStoreQueryResult
from aws_utils.secrets_manager import get_secret
import time


class WeaviateStorageRetriever: 
    def __init__(self):
        kclogger.info(f"WeaviateStorageRetriever::init called")
        url = get_secret('WeaviateUrl')
        weaviate_key = get_secret('WeaviateApiKey')
        auth_config = AuthApiKey(api_key=weaviate_key)
        self.weaviate_client = weaviate.Client(url, auth_client_secret=auth_config)

    def query(self, embedding: list[float], top_k: int, schema: str) -> VectorStoreQueryResult:
        start_time = time.time()
        weaviate_store = WeaviateVectorStore(weaviate_client=self.weaviate_client, index_name=schema)
        store_query = VectorStoreQuery(query_embedding=embedding, similarity_top_k=top_k, mode="default")
        result = weaviate_store.query(store_query)
        kclogger.info(f"WeaviateStorageRetriever::query took {time.time() - start_time} seconds")
        return result