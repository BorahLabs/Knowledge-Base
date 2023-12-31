from dataclasses import dataclass

@dataclass
class VectorSearchResult:
    id: int
    entity: str
    score: float
    text: str
    payload: dict
