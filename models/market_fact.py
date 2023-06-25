from pydantic import BaseModel
from models.order import orders
from models.product import product
from models.shipping import Shipping


class Market_Fact_Model(BaseModel):
    order : orders
    product : product
    shipping : Shipping
    days_taken_for_delivery: int
    sales : float
    discount :float
    order_Quantity :int
    profit :float
    shipping_Cost :float
    product_base_margin :float
    # def __repr__(self):
    #         return {
    #             "Product Id":self.prod_id,
    #             "Order Id":self.ord_id,
    #             "Shipping Id":self.ship_id,
    #             "Customer Id":self.cust_id,
    #             "Sales":self.sales,
    #             "Discount":self.discount,
    #             "Order Quantity":self.order_Quantity,
    #             "Profit":self.profit,
    #             "Shipping Cost":self.shipping_Cost,
    #             "Product Base Margin":self.product_base_margin
    #         }