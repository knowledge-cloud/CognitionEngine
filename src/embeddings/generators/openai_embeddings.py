import time
from typing import List

from langchain.embeddings.openai import OpenAIEmbeddings

from aws_utils.secrets_manager import get_secret
from utils.log_utils import kclogger


class OpenAIEmbeddingsUtils:
    def __init__(self):
        kclogger.info(f"OpenAIEmbeddingsUtils::init called")
        openaiApiKey = get_secret('OpenAiSecretKey')
        self.model = OpenAIEmbeddings(openai_api_key=openaiApiKey)

    def generate_embedding(self, text: str) -> List[float]:
        start_time = time.time()
        kclogger.info(
            f"OpenAIEmbeddingsUtils::generate_embedding generating embedding for text: {text}")
        embedding = self.model.embed_query(text)
        kclogger.info(
            f"OpenAIEmbeddings::generate_embedding took {time.time() - start_time} seconds")
        return embedding
