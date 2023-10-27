import time
from typing import List

from langchain.schema.document import Document
from langchain.vectorstores import weaviate

from aws_utils.secrets_manager import get_secret
from utils.constants import WEAVIATE_URL
from utils.log_utils import kclogger


class WeaviateStorageRetriever:
    def __init__(self):
        kclogger.info(f"WeaviateStorageRetriever::init called")
        weaviate_key = get_secret('WeaviateApiKey')
        self.weaviate_client = weaviate._create_weaviate_client(
            url=WEAVIATE_URL, api_key=weaviate_key)

    def query(self, embedding: list[float], top_k: int, schema: str) -> List[Document]:
        start_time = time.time()
        attributes = ["text"]
        weaviate_store = weaviate.Weaviate(
            client=self.weaviate_client,
            index_name=schema,
            text_key="text",
            attributes=attributes
        )
        result = weaviate_store.similarity_search_by_vector(
            embedding=embedding, k=top_k, include_vector=False)
        kclogger.info(
            f"WeaviateStorageRetriever::query fetched total of {len(result)} results")
        kclogger.info(
            f"WeaviateStorageRetriever::query took {time.time() - start_time} seconds")
        return result
