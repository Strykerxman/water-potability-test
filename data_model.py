from pydantic import BaseModel
from typing import Optional

class NewStudent(BaseModel):
    name: str
    age: int

class UpdateStudent(BaseModel):
    name: Optional[str]
    age: Optional[int]