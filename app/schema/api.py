from pydantic import BaseModel
from datetime import datetime


class APICreate(BaseModel):
    name: str
    url: str
    method: str = "GET"
    
class APIResponse(BaseModel):
    id: int
    name: str
    url: str
    method: str
    created_at: datetime

    class Config:
        from_attributes = True