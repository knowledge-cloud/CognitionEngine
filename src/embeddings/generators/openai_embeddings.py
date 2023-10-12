from typing import List
from dotenv import load_dotenv
from llama_index.embeddings import OpenAIEmbedding
import os
from utils.log_utils import kclogger

class OpenAIEmbeddings:
    def __init__(self):
        load_dotenv()
        openaiApiKey = os.environ.get('OPENAI_API_KEY')
        kclogger.info(f"OpenAIEmbeddings::init openaiApiKey: {openaiApiKey}")
        self.model = OpenAIEmbedding(api_key=openaiApiKey)

    def generate_embedding(self, text: str) -> List[float]:
        return self.model.get_query_embedding(text)
    