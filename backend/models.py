from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Favorite(BaseModel):
    id: int
    name: str
    image: str
    nickname: str = ""
    created_at: Optional[datetime] = None

class FavoriteInDB(Favorite):
    _id: Optional[str] = None