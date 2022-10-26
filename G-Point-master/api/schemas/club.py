
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field


class Club(BaseModel):
    clubId: str = Field(None, example="999999")
    description: str = Field(None, example="テスト用サークル")
    point: list = Field(None, description='[1, 2, 3]')
    type: int = Field(None, description="1")
