from database import SessionClass
from schemas.product_dimension import Product_Dimension
from schemas.market_fact import Market_Fact
from models.sales import Sales,Profit
from sqlalchemy.sql import func
from fastapi import HTTPException
import logging

logger=logging.getLogger(__name__)

sql1 = SessionClass()
sql = sql1.get_session()

def get_sales():
    try:
        query = sql.query(
            Market_Fact.prod_id,
            func.sum(Market_Fact.sales)
        ).group_by(
            Market_Fact.prod_id
        ).all()
        logger.info("Getting product and grouping by sales")
        if query is None:
            return "No sale has been done"
        sale = dict()
        for i in query:
            sale[i[0]]=i[1]
        logger.info(f"Product and sales info")
        return sale
    except:
        logger.error("No sales has been done")


def get_profit():
    try:
        query = sql.query(
            Market_Fact.prod_id,
            func.sum(Market_Fact.profit)
            ).group_by(
            Market_Fact.prod_id
            ).all()
        logger.info("Getting product and grouping by Profit")
        if query is None:
            return "No sale has been done"
        profit = dict()
        for i in query:
            profit[i[0]]=i[1]
        return profit
    except:
        logger.error("No sales has been done")


