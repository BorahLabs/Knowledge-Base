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
