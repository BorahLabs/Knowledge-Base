import dotenv
import os
from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict
from typing import List

from embeddings.HuggingfaceModel import HuggingfaceModel
from reranking.HuggingfaceRerankingModel import HuggingfaceRerankingModel
from vector_database.QdrantVectorDatabase import QdrantVectorDatabase
from vector_database.dto.InsertData import InsertData

dotenv.load_dotenv()

class InsertItem(BaseModel):
    id: int
    entity: str
    text: str
    payload: dict = None

class InsertBody(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    data: List[InsertItem]

vector_database = QdrantVectorDatabase()
embeddings_model = HuggingfaceModel(os.getenv('EMBEDDINGS_MODEL_NAME'))
reranking_model = HuggingfaceRerankingModel(os.getenv('RERANKING_MODEL_NAME'))

app = FastAPI()

@app.post('/insert')
def insert(body: InsertBody):
    embeddings = embeddings_model.embed_many([item.text for item in body.data])
    data = [InsertData(id=item.id, text=item.text, entity=item.entity, vector=vector, payload=item.payload) for item, vector in zip(body.data, embeddings)]
    vector_database.insert(data)
    return {
        'success': True,
    }

@app.get('/query')
def query(query: str, k: int = 5, entities: str = None):
    vector = embeddings_model.embed_one(query)
    results = vector_database.query(vector, k, entities=entities)
    if len(results) == 0:
        return {
            'success': True,
            'results': [],
        }

    reranked_results = reranking_model.rerank(query, results)
    return {
        'success': True,
        'results': reranked_results,
    }
