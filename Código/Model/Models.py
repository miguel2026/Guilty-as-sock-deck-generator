from pydantic import BaseModel
from typing import Optional

class Card(BaseModel):
    id: int
    deck_id: int
    name: str
    description: Optional[str] = None
    image_url: Optional[str] = None

class Deck(BaseModel):
    id: int
    user_id: int
    name: str
    description: Optional[str] = None
    cards: list[Card]
class User(BaseModel):
    id: int
    language: str = 'en'
    username: str
    email: str
    password: str
    decks: Optional[list[Deck]] = None