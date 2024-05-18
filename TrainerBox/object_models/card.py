from typing import Optional, List
from pydantic import BaseModel, Field
import uuid

class Card(BaseModel):
    # uuid unique to the card
    id: str
    # name of card
    name: str = Field(min_length=1)
    # type of card (e.g. Pokemon, baseball, etc.)
    category: str = Field(min_length=1)
    # pull from card's description
    description: str = Field(min_lenth=1, max_length=100)
    # current best guess market value
    price: float = Field(gt=0, decimal_places=2)
    # user managed tags
    user_tags: List[str]

    def __init__(self, id, name, category, description, price):
        self.id = id
        self.name = name
        self.category = category
        self.description = description
        self.price = price
        
    class Example:
        json_schema_example = {
            "example": {
                "id": uuid.uuid1(),
                "name": "Charmander",
                "category": "Pokemon",
                "description": "Lizard pokemon",
                "price": 3.24,
                "user_tags": ["favorite"]
            }
        }
