from abc import ABC, abstractmethod

class EmbeddingsModelContract(ABC):
    def __init__(self, model_name: str):
        self.model_name = model_name

    @abstractmethod
    def embed(self, text: str):
        pass

    def embed_one(self, text: str):
        return self.embed([text])[0]

    def embed_many(self, texts: list):
        return self.embed(texts)
