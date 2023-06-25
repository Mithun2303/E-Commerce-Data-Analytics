from pydantic import BaseModel
from typing import List
from models.market_fact import Market_Fact_Model
from typing import List

class customer_model(BaseModel):
    customer_name:str
    province :str
    region :str
    no_of_orders : int
    orders_placed : List[Market_Fact_Model]
    # def __dict__(self):
    #     return {
    #         "Name":self.customer_name,
    #         "Province":self.province,
    #         "Region":self.region,
    #         "Orders Placed":self.orders_placed
    #     }
