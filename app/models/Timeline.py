from typing import List
from pydantic import BaseModel

class Timeline(BaseModel):
    id: str
    date: str
    events: List[str]
    completed:bool = False
