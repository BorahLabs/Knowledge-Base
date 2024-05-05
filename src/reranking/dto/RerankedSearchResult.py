from dataclasses import dataclass


@dataclass
class RerankedSearchResult:
    id: int
    entity: str
    text: str
    score: float
    payload: dict
