
from typing import Optional

from pydantic import BaseModel, Field


class User(BaseModel):
    userId: str = Field(None, example="999999")
    point: int = Field(None, example=300)
    history: list = Field(None, description="滞在履歴")
    prize: dict = Field(None, description="交換履歴")
    
class History(BaseModel):
    clubId: str
    point: int
    timeStamp: str
class Item(BaseModel):
    name: str