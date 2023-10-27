from enum import Enum
from typing import List

from embeddings.generators.openai_embeddings import OpenAIEmbeddingsUtils
from utils.log_utils import kclogger


class EmbeddingSource(Enum):
    OPENAI = "OPENAI"
    LLAMA_INDEX = "LLAMA_INDEX"


class EmbeddingGenerator:
    class EmbeddingGeneratorException(Exception):
        pass

    def generate_embedding(self, text: str, embedding_source: EmbeddingSource) -> List[float]:
        kclogger.info(
            f"EmbeddingGenerator::generate_embedding called with text: {text} and embedding_source: {embedding_source}")
        match embedding_source:
            case EmbeddingSource.OPENAI:
                return self._generate_openai_embedding(text)
            case default:
                raise self.EmbeddingGeneratorException(
                    "Invalid embedding source")

    def _generate_openai_embedding(self, text: str):
        return OpenAIEmbeddingsUtils().generate_embedding(text)


EmbeddingGeneratorInstance = EmbeddingGenerator()
