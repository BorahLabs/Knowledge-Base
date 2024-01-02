from abc import ABC, abstractmethod
from typing import List
from vector_database.dto.InsertData import InsertData

class VectorDatabaseContract(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def insert(self, data: List[InsertData]):
        pass

    @abstractmethod
    def query(self, vector, k, **kwargs):
        pass

    @abstractmethod
    def delete(self, ids: List[str]):
        pass

    @abstractmethod
    def update(self, data: List[InsertData]):
        pass
