import os
from typing import Dict, Any
from langchain_community.vectorstores import Qdrant
from qdrant_client.http import models

from vector_database.contracts.VectorDatabaseContract import VectorDatabase


class QdrantVectorDatabase(VectorDatabase):
    @staticmethod
    def make() -> 'QdrantVectorDatabase':
        from env import get_embeddings_model

        collection_name = os.getenv('EMBEDDINGS_COLLECTION_NAME', 'embeddings')
        store = Qdrant.construct_instance(
            texts=['Test'],
            embedding=get_embeddings_model(),
            location=':memory:' if os.getenv('QDRANT_HOST') is None else None,
            host=os.getenv('QDRANT_HOST'),
            port=os.getenv('QDRANT_PORT', 6333),
            collection_name=collection_name,
        )

        try:
            store.client.create_payload_index(
                collection_name="embeddings",
                field_name="entity",
                field_schema="keyword",
            )
        except:
            pass

        return QdrantVectorDatabase(
            store=store,
        )

    def get_search_kwargs(self, entities: str, filters: Dict[str, Any]) -> Dict[str, Any]:
        must_filters = []
        if entities is not None:
            entities = entities.split(',')
            must_filters.append(models.FieldCondition(
                key='metadata.entity',
                match=models.MatchAny(any=entities)
            ))

        if filters is not None and len(filters) > 0:
            for key, value in filters.items():
                if isinstance(value, str):
                    value = value.split(',')

                if not isinstance(value, list):
                    value = [value]

                must_filters.append(models.FieldCondition(
                    key=f'metadata.payload.{key}',
                    match=models.MatchAny(any=value),
                ))

        return {
            'filter': models.Filter(
                must=must_filters,
            )
        }
