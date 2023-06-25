from database import Base

from sqlalchemy import (
    String,
    Column,
    )

class Customer_Dimension(Base):
    __tablename__ = "customerdimension"
    customer_name = Column(String, nullable = False)
    province = Column(String,nullable = False)
    region = Column(String, nullable = False)
    customer_segment = Column(String )
    customer_id = Column(String,primary_key=True)
    def __repr__(self):
        return {
            "name":self.customer_name,
            "province":self.province,
            "region":self.region,
            "customer segment":self.customer_segment,
            "customer id":self.customer_id
        }