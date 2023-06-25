from database import Base
from .order_dimension import Order_Dimension
from sqlalchemy import (
    String,
    Column,
    Integer,
    ForeignKey,
    DATE,

    )

class Shipping_Dimension(Base):
    __tablename__ = "shippingdimension"
    order_id = Column(Integer ,nullable = False )
    shipping_mode = Column(String)
    shipping_date = Column(DATE)
    shipping_id = Column(String, nullable = False, primary_key = True)

    def __repr__(self):
        return {
            "Order Id" : self.order_id,
            "Shipping Mode" : self.shipping_mode,
            "Shipping Date" : self.shipping_date,
            "Shipping Id" : self.shipping_id
        }