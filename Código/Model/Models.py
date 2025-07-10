from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: int
    username: str
    email: str
    password: str

class Deck(BaseModel):
    id: int
    user_id: int
    name: str
    description: Optional[str] = None

class Card(BaseModel):
    id: int
    deck_id: int
    name: str
    description: Optional[str] = None
    image_url: Optional[str] = None