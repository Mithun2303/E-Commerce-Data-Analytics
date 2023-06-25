from pydantic import BaseModel

class Custorder(BaseModel):
    cust_id : str
    cust_name : str
    cust_province : str
    cust_region : str
    no_of_order : int
    def  __str__(self):
        return {
            "name":self.cust_name,
            "province":self.province,
            "region":self.region,
            "customer id":self.cust_id,
            "no of orders" : self.no_of_order
        }