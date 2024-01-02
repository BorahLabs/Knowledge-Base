from pydantic import BaseModel, ConfigDict
from typing import List

class InsertItem(BaseModel):
    id: any
    entity: str
    text: str
    payload: dict = None

class InsertBody(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    data: List[InsertItem]
