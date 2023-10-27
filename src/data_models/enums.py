from enum import Enum


class EventType(Enum):
    RETRIEVAL = "RETRIEVAL"
    INGESTION = "INGESTION"


class KnowledgeBaseIndex(Enum):
    UPSC = "UpscIndex"
    KC = "KCIndex"
