from sentence_transformers import SentenceTransformer
from typing import List
from embeddings.contracts.EmbeddingsModelContract import EmbeddingsModelContract

class HuggingfaceModel(EmbeddingsModelContract):
    def __init__(self, model_name: str):
        super().__init__(model_name)
        self.model = SentenceTransformer(model_name)

    def embed(self, texts: List[str]):
        return self.model.encode(texts, normalize_embeddings=True)
