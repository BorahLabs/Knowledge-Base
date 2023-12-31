from dataclasses import dataclass

@dataclass
class InsertData:
    id: int
    entity: str
    text: str
    vector: any
    payload: dict = None
