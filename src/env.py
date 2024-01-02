import os

from vector_database.contracts.VectorDatabaseContract import VectorDatabaseContract
from vector_database.QdrantVectorDatabase import QdrantVectorDatabase

from embeddings.contracts.EmbeddingsModelContract import EmbeddingsModelContract
from embeddings.HuggingfaceModel import HuggingfaceModel

from reranking.contracts.RerankingModelContract import RerankingModelContract
from reranking.HuggingfaceRerankingModel import HuggingfaceRerankingModel

def get_vector_database() -> VectorDatabaseContract:
    if os.getenv('VECTOR_DATABASE', 'qdrant') == 'qdrant':
        return QdrantVectorDatabase()

    raise Exception('Unknown vector database')

def get_embeddings_model() -> EmbeddingsModelContract:
    if os.getenv('EMBEDDINGS_MODEL', 'huggingface') == 'huggingface':
        return HuggingfaceModel(os.getenv('EMBEDDINGS_MODEL_NAME'))

    raise Exception('Unknown embeddings model')

def get_reranking_model() -> RerankingModelContract:
    if os.getenv('RERANKING_MODEL', 'huggingface') == 'huggingface':
        return HuggingfaceRerankingModel(os.getenv('RERANKING_MODEL_NAME'))

    raise Exception('Unknown reranking model')
