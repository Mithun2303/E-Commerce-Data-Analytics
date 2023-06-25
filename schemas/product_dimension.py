from database import Base
from sqlalchemy import (
    String,
    Column,
    )

class Product_Dimension(Base):
    __tablename__ = 'productdimension'
    product_category = Column(String , nullable = False)
    product_sub_category = Column(String , nullable = True)
    product_id = Column(String , primary_key = True)

    def __repr__(self):
        return {
            "Product Category" : self.product_category,
            "Product Sub Category" : self.product_sub_category,
            "Product Id" : self.product_id
        }