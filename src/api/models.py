from pydantic import BaseModel, ConfigDict
from typing import List, Union


class InsertItem(BaseModel):
    id: Union[str, int]
    entity: str
    text: str
    payload: dict = None


class InsertBody(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    data: List[InsertItem]


class ChunkItem(BaseModel):
    id: Union[str, int]
    text: str


class ChunkBody(BaseModel):
    data: List[ChunkItem]
    chunk_size: int = 0
    chunk_overlap: int = 0
