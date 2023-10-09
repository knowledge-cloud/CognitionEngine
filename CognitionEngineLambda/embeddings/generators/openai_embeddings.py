from llama_index.embeddings import OpenAIEmbedding
from llama_index.embeddings.openai import OpenAIEmbeddingModelType

class OpenAIEmbeddings:
    def __init__(self):
        self.model = OpenAIEmbedding()

    def generate_embedding(self, text):
        return self.model.get_query_embedding(text)
    