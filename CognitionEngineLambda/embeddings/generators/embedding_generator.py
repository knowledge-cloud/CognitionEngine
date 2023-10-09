from enum import Enum
from embeddings.generators.openai_embeddings import OpenAIEmbeddings

class EmbeddingGeneratorError(Exception):
    pass

class EmbeddingSource(Enum):
    OPENAI = "OPENAI"
    LLAMA_INDEX = "LLAMA_INDEX"


class EmbeddingGenerator:
    def __init__(self):
        self.openai_embedding_generator = OpenAIEmbeddings()
    
    def generateEmbedding(self, text, embedding_source: EmbeddingSource):
        if embedding_source == EmbeddingSource.OPENAI:
            return self.openai_embedding_generator.generate_embedding(text)
        else:
            raise EmbeddingGeneratorError("Invalid embedding source")
        