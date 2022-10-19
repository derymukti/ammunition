from pydantic import BaseModel
from typing import Dict, List, Optional
import pydantic

from modules.example.entity import Result

class CreateRequestDTO(BaseModel):
    """Create Request DTO"""
    id: Optional[int]
    url: str
    result_all: Dict
    result_no_stop_words: Dict

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class ListDTO(BaseModel):
    list: List[CreateRequestDTO] = []
    class Config:
        orm_mode = True