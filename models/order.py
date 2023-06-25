from pydantic import BaseModel


class orders(BaseModel):
    order_id :str 
    order_date :str
    order_priority :str


