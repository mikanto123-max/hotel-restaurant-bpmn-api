from pydantic import BaseModel
from typing import Optional

class Room(BaseModel):
    id: int
    category: str
    price_per_night: float
    is_clean: bool = True

class Reservation(BaseModel):
    id: Optional[int] = None
    client_name: str
    client_id_number: str
    room_id: int
    nights: int
    total_amount: float = 0
    invoice_number: str = ""