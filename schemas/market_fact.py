from database import Base

from schemas.customer_dimension import Customer_Dimension
from schemas.order_dimension import Order_Dimension
from schemas.product_dimension import Product_Dimension
from schemas.shipping_dimension import Shipping_Dimension

from sqlalchemy import (
    Column,
    String,
    ForeignKey,
    INTEGER,
    Numeric
)
class Market_Fact(Base):
    __tablename__='marketfact'
    sno = Column(INTEGER,primary_key=True)
    ord_id = Column(String,ForeignKey(Order_Dimension.ord_id))
    prod_id = Column(String,ForeignKey(Product_Dimension.product_id))
    ship_id = Column(String , ForeignKey(Shipping_Dimension.shipping_id))
    cust_id = Column(String)
    sales = Column(Numeric)
    discount = Column(Numeric)
    order_Quantity = Column(INTEGER) 
    profit = Column(Numeric) 
    shipping_Cost = Column(Numeric) 
    product_base_margin = Column(Numeric)

    def __repr__(self):
        return {
            "Product Id":self.prod_id,
            "Order Id":self.ord_id,
            "Shipping Id":self.ship_id,
            "Customer Id":self.cust_id,
            "Sales":self.sales,
            "Discount":self.discount,
            "Order Quantity":self.order_Quantity,
            "Profit":self.profit,
            "Shipping Cost":self.shipping_Cost,
            "Product Base Margin":self.product_base_margin
        }