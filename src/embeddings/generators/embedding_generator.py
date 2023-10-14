from enum import Enum
from typing import List
from utils.log_utils import kclogger
from embeddings.generators.openai_embeddings import OpenAIEmbeddings


class EmbeddingGeneratorError(Exception):
    pass

class EmbeddingSource(Enum):
    OPENAI = "OPENAI"
    LLAMA_INDEX = "LLAMA_INDEX"


class EmbeddingGenerator:
    def __init__(self):
        self.openai_embedding_generator = OpenAIEmbeddings()
    
    def generate_embedding(self, text: str, embedding_source: EmbeddingSource) -> List[float]:
        kclogger.info(f"EmbeddingGenerator::generate_embedding called with text: {text} and embedding_source: {embedding_source}")
        if embedding_source == EmbeddingSource.OPENAI:
            return self.openai_embedding_generator.generate_embedding(text)
        else:
            raise EmbeddingGeneratorError("Invalid embedding source")
        
EmbeddingGeneratorInstance = EmbeddingGenerator()
generate_embedding = EmbeddingGeneratorInstance.generate_embedding