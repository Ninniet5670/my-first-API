from pydantic import BaseModel 

class Sale(BaseModel):
    id: int
    item: str
    unit_price: float
    quantity: int
