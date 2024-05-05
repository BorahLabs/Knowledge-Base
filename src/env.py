import os
import json

from langchain_core.embeddings import Embeddings
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from flashrank import Ranker

from vector_database.contracts.VectorDatabaseContract import VectorDatabase
from vector_database.QdrantVectorDatabase import QdrantVectorDatabase


def get_vector_database() -> VectorDatabase:
    db = os.getenv('VECTOR_DATABASE', 'qdrant')
    if db == 'qdrant':
        return QdrantVectorDatabase.make()

    raise Exception('Unknown vector database')


def get_embeddings_model() -> Embeddings:
    embeddings_provider = os.getenv('EMBEDDINGS_PROVIDER', 'huggingface')
    model_kwargs = json.loads(os.getenv('EMBEDDINGS_MODEL_KWARGS', '{}'))
    encode_kwargs = json.loads(os.getenv('EMBEDDINGS_ENCODE_KWARGS', '{}'))
    model_name = os.getenv('EMBEDDINGS_MODEL_NAME')

    if embeddings_provider == 'huggingface':
        return HuggingFaceEmbeddings(
            model_name=model_name,
            model_kwargs=model_kwargs,
            encode_kwargs=encode_kwargs
        )

    if embeddings_provider == 'openai':
        return OpenAIEmbeddings(
            model=model_name,
            model_kwargs=model_kwargs,
        )

    raise Exception('Unknown embeddings model')


def get_reranking_model() -> Ranker:
    reranking_model = os.getenv('RERANKING_MODEL')
    if reranking_model is None:
        return Ranker()

    return Ranker(model_name=reranking_model, cache_dir=os.getenv('RERANKING_CACHE_DIR', '/opt'))
