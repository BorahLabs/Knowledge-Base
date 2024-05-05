from abc import ABC
from typing import Dict, Any
from langchain.vectorstores import VectorStore


class VectorDatabase(ABC):
    store: VectorStore

    def __init__(self, store: VectorStore):
        self.store = store

    @staticmethod
    def make() -> 'VectorDatabase':
        pass

    def get_search_kwargs(self, entities: str, filters: Dict[str, Any]) -> Dict[str, Any]:
        pass
