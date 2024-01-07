import dotenv
import env

from fastapi import FastAPI
from api.models import InsertBody
from vector_database.dto.InsertData import InsertData


dotenv.load_dotenv()

vector_database = env.get_vector_database()
embeddings_model = env.get_embeddings_model()
reranking_model = env.get_reranking_model()

app = FastAPI()

@app.get('/status')
def status():
    return {
        'status': 'ok',
    }

@app.post('/insert')
def insert(body: InsertBody):
    embeddings = embeddings_model.embed_many([item.text for item in body.data])
    data = [InsertData(id=item.id, text=item.text, entity=item.entity, vector=vector, payload=item.payload) for item, vector in zip(body.data, embeddings)]
    vector_database.insert(data)
    return {
        'success': True,
    }

@app.delete('/delete/{id}')
def delete(id):
    vector_database.delete([id])
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
