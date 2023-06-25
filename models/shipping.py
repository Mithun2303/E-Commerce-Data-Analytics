from pydantic import BaseModel


class Shipping(BaseModel):
    mode : str
    id : str
    date : str