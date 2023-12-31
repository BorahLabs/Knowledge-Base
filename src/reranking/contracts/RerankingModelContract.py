from abc import ABC, abstractmethod
from typing import List
from vector_database.dto.VectorSearchResult import VectorSearchResult

class RerankingModelContract(ABC):
    def __init__(self, model_name: str):
        self.model_name = model_name

    @abstractmethod
    def rerank(self, query: str, documents: List[VectorSearchResult]):
        pass
