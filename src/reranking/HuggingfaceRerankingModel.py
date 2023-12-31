import os
from typing import List
from sentence_transformers import CrossEncoder

from reranking.contracts.RerankingModelContract import RerankingModelContract
from reranking.dto.RerankedSearchResult import RerankedSearchResult
from vector_database.dto.VectorSearchResult import VectorSearchResult

class HuggingfaceRerankingModel(RerankingModelContract):
    def __init__(self, model_name: str):
        super().__init__(model_name)
        self.model = CrossEncoder(model_name, max_length=int(os.getenv('RERANKING_MAX_LENGTH', 512)))

    def rerank(self, query: str, documents: List[VectorSearchResult]) -> List[RerankedSearchResult]:
        scores = self.model.predict([(query, doc.text) for doc in documents]).tolist()
        results = [
            RerankedSearchResult(
                id=doc.id,
                entity=doc.entity,
                text=doc.text,
                vector_score=doc.score,
                reranking_score=score,
                payload=doc.payload,
            ) for doc, score in zip(documents, scores)
        ]
        results.sort(key=lambda x: x.reranking_score, reverse=True)
        return results
