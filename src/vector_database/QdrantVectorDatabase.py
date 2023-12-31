from vector_database.contracts.VectorDatabaseContract import VectorDatabaseContract
from vector_database.dto.InsertData import InsertData
from vector_database.dto.VectorSearchResult import VectorSearchResult
import os
from typing import List
from qdrant_client import QdrantClient
from qdrant_client.http import models

class QdrantVectorDatabase(VectorDatabaseContract):
    COLLECTION_NAME = 'embeddings'

    def __init__(self):
        self.client = QdrantClient(':memory:')
        self.client.create_collection(
            collection_name=self.COLLECTION_NAME,
            vectors_config=models.VectorParams(size=os.getenv('EMBEDDINGS_VECTOR_SIZE'), distance=models.Distance.COSINE),
        )

    def insert(self, data: List[InsertData]):
        self.client.upsert(
            collection_name=self.COLLECTION_NAME,
            points=[
                models.PointStruct(
                    id=item.id,
                    payload={
                        **(item.payload if item.payload is not None else {}),
                        "id": item.id,
                        "entity": item.entity,
                        "text": item.text,
                    },
                    vector=item.vector,
                ) for item in data
            ]
        )

    def query(self, vector, k, **kwargs) -> List[VectorSearchResult]:
        must_filters = []
        if kwargs.get('entities') is not None:
            entities = kwargs.get('entities').split(',')
            must_filters.append(models.FieldCondition(
                key='entity',
                match=models.MatchAny(any=entities)
            ))

        results = self.client.search(
            collection_name=self.COLLECTION_NAME,
            query_vector=vector,
            limit=k,
            query_filter=models.Filter(
                must=must_filters,
            ),
        )

        return [
            VectorSearchResult(
                id=result.id,
                entity=result.payload['entity'],
                text=result.payload['text'],
                score=result.score,
                payload=result.payload,
            ) for result in results
        ]
