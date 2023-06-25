from pydantic import BaseModel

class Sales(BaseModel):
    prod_id:str
    sales:float
    def __dict__(self):
        return {
            "Product ID":self.prod_id,
            "Sales":self.sales
        }
    
class Profit(BaseModel):
    prod_id:str
    profit:float
    def __dict__(self):
        return {
            "Product ID":self.prod_id,
            "Profit":self.profit
        }