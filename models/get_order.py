from pydantic import BaseModel
from models.product import product
from models.shipping import Shipping
from models.customer import customer_model
from models.custorder import Custorder
from models.order import orders

class Get_Orders(BaseModel):
    order : orders
    delivered_in : int
    ship : Shipping
    cust : Custorder
    prod : product
    def __dict__(self):
        return {
            "Order Details":self.order,
            "Delivered in":self.delivered_in,
            "Customer Details":self.cust,
            "Product Details":self.order,
            "Shipment Details":self.ship
        }