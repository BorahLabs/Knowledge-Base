from dataclasses import dataclass

@dataclass
class RerankedSearchResult:
    id: int
    entity: str
    text: str
    vector_score: float
    reranking_score: float
    payload: dict
