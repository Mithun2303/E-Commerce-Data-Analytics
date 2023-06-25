from database import SessionClass
from schemas.market_fact import Market_Fact
from schemas.customer_dimension import Customer_Dimension
from models.custorder import Custorder
import sqlalchemy
from sqlalchemy import desc
from fastapi import HTTPException
import logging


logger = logging.getLogger(__name__)

sql1 = SessionClass()
sql = sql1.get_session()

def get_max_order(number,off_set):
    try:
        max_cust = sql.query(
            Market_Fact.cust_id,
            sqlalchemy.func.count(Market_Fact.cust_id)
            ).group_by(
            Market_Fact.cust_id
            ).order_by(
            desc(sqlalchemy.func.count(Market_Fact.cust_id))
            ).order_by(
            desc(Market_Fact.cust_id)
            ).offset(
                off_set
            ).limit(
                number
            )
        if max_cust is None:
            raise IndexError
        dictobj =dict()
        for i in range(number):
            cust_details = sql.query(
                Customer_Dimension
            ).filter(
                Customer_Dimension.customer_id == max_cust[i][0]
            ).first()
            
            dictobj[cust_details.customer_id]=Custorder(
                cust_id = cust_details.customer_id,
                cust_name = cust_details.customer_name,
                cust_province = cust_details.province,
                cust_region = cust_details.region,
                no_of_order =  max_cust[i][1]
            )
        return dictobj
    except IndexError as e:
        logger.error("INDEX out of range")
        return "Customer index out of range"