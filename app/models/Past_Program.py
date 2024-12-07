from typing import List
from pydantic import BaseModel

class Program(BaseModel):
    title: str
    year:str
    technology: str
    description: str
    mentor:str
    mentee:List[str]
    codelink:str