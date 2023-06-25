from database import Base
from .product_dimension import Product_Dimension
from sqlalchemy import (
    String,
    Column,
    INTEGER,
    ARRAY,
    DATE,
    ForeignKey
    )

class Order_Dimension(Base):
    __tablename__ = "orderdimension"
    order_id = Column(INTEGER,nullable = False, )
    order_date = Column(DATE,nullable = False, )
    order_priority = Column(String)
    ord_id = Column((String),primary_key=True)

    def __repr__(self):
        return {
            "Order Id" : self.order_id,
            "Order Date" : self.order_date,
            "Order Priority" : self.order_priority,
            "ord_id" : self.ord_id
        }