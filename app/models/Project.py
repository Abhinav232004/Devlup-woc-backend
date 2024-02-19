from pydantic import BaseModel

class Project(BaseModel):
    id: int
    title: str
    tag:str
    technology: str
    description: str
    mentor:str
