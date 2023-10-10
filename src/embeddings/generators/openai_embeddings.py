from typing import List
from llama_index.embeddings import OpenAIEmbedding
import os

class OpenAIEmbeddings:
    def __init__(self):
        openaiApiKey = os.environ.get("OPENAI_API_KEY")
        self.model = OpenAIEmbedding(api_key=openaiApiKey)

    def generate_embedding(self, text: str) -> List[float]:
        return self.model.get_query_embedding(text)
    