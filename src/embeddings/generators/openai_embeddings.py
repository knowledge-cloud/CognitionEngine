from typing import List
from utils.log_utils import kclogger
from llama_index.embeddings import OpenAIEmbedding
from aws_utils.secrets_manager import get_secret
import os
import time

class OpenAIEmbeddings:
    def __init__(self):
        kclogger.info(f"OpenAIEmbeddings::init called")
        openaiApiKey = get_secret('OpenAiSecretKey')
        os.environ["OPENAI_API_KEY"] = openaiApiKey
        self.model = OpenAIEmbedding()

    def generate_embedding(self, text: str) -> List[float]:
        start_time = time.time()
        embedding = self.model.get_query_embedding(text)
        kclogger.info(f"OpenAIEmbeddings::generate_embedding took {time.time() - start_time} seconds")
        return embedding
    