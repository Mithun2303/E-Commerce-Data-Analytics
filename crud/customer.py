from database import SessionClass
from schemas.customer_dimension import Customer_Dimension
from schemas.market_fact import Market_Fact
from schemas.product_dimension import Product_Dimension
from schemas.order_dimension import Order_Dimension
from schemas.shipping_dimension import Shipping_Dimension
from models.customer import customer_model
from models.market_fact import Market_Fact_Model
from models.order import orders
from models.product import product
from models.shipping import Shipping
from schemas.order_dimension import Order_Dimension
from schemas.market_fact import Market_Fact
from datetime import date
from sqlalchemy.sql import extract, distinct, and_
from sqlalchemy import func
import logging
from fastapi import HTTPException

logger = logging.getLogger(__name__)


sql1 = SessionClass()
sql = sql1.get_session()


def get_details(id: str):
    id = id.capitalize()
    logger.info(f"ID ={id}")
    try:
        check_id = sql.query(Customer_Dimension).filter(
            Customer_Dimension.customer_id == id).first()
        logger.info(f"Checking for existenct of customer: {id}")

        if check_id is None:
            logger.error("ID not found")
            return "Customer Not Found"
        
        try:
            count_order = sql.query(
                Market_Fact.ord_id
            ).filter(
                Market_Fact.cust_id == id
            ).count()
            logger.info(
                f"Getting count of orders by the customer:{count_order}")
        
            if not count_order:
                logger.error("Customer have zero order")
                return "Customer have zero order"
        
            pso_details = sql.query(
                Market_Fact,
                Product_Dimension,
                Shipping_Dimension,
                Order_Dimension
            ).join(
                Product_Dimension
            ).join(
                Order_Dimension
            ).join(
                Shipping_Dimension
            ).filter(
                Market_Fact.cust_id == id
            ).all()
        
            logger.info(
                f"Getting product,shipping,order details for customer {id}")
        
            ls = list()
        
            for i in range(count_order):
                order_obj = orders(
                    order_id=(pso_details[i].Order_Dimension.ord_id),
                    order_date=str(pso_details[i].Order_Dimension.order_date),
                    order_priority=pso_details[i].Order_Dimension.order_priority
                )
                ord_date = pso_details[i].Order_Dimension.order_date
                product_obj = product(
                    product_category=pso_details[i].Product_Dimension.product_category,
                    product_sub_category=pso_details[i].Product_Dimension.product_sub_category,
                    product_id=pso_details[i].Product_Dimension.product_id
                )
                shipping_obj = Shipping(
                    mode=pso_details[i].Shipping_Dimension.shipping_mode,
                    date=str(pso_details[i].Shipping_Dimension.shipping_date),
                    id=pso_details[i].Shipping_Dimension.shipping_id
                )
                ship_date = pso_details[i].Shipping_Dimension.shipping_date
                day_until = (((ship_date-ord_date).days))
                mar_fact_obj = Market_Fact_Model(
                    order=order_obj,
                    shipping=shipping_obj,
                    product=product_obj,
                    days_taken_for_delivery=day_until,
                    sales=pso_details[i].Market_Fact.sales,
                    discount=pso_details[i].Market_Fact.discount,
                    order_Quantity=pso_details[i].Market_Fact.order_Quantity,
                    profit=pso_details[i].Market_Fact.profit,
                    shipping_Cost=pso_details[i].Market_Fact.shipping_Cost,
                    product_base_margin=pso_details[i].Market_Fact.product_base_margin
                )
                ls.append(mar_fact_obj)
            cust_obj = customer_model(
                customer_name=check_id.customer_name,
                province=check_id.province,
                region=check_id.region,
                no_of_orders=count_order,
                orders_placed=ls
            )
            return (cust_obj)
        
        except AttributeError as e:
            logger.error("Error while getting number of order\ncustomer have zero")
    except Exception as e:
        logger.error(f"Error while getting customer ID : {id}")


def get_unique_customer():
    try:
        ord_id = sql.query(
            Order_Dimension.ord_id
        ).filter(
            and_(
                Order_Dimension.order_date >= '2011-01-01',
                Order_Dimension.order_date <= '2011-12-31'
            )
        ).subquery()
        
        logger.info("Getting number of orders placed between given time period as a subquery")

        if ord_id is None:
            logger.error("No orders where placed between the given time")
            return "No order found"
        
        cust_id = sql.query(
            distinct(Market_Fact.cust_id)
        ).join(
            Order_Dimension,
            Market_Fact.ord_id == Order_Dimension.ord_id
        ).filter(
            and_(
                extract("month", Order_Dimension.order_date) == 1,
                extract("year", Order_Dimension.order_date) == 2011
            )
        ).subquery()

        logger.info("Getting distinct customer id who purchased through the time as a subquery")

        subquery1 = sql.query(
            Market_Fact.cust_id,
            Market_Fact.ord_id,
            Order_Dimension.order_date
        ).join(
            Order_Dimension,
            Market_Fact.ord_id == Order_Dimension.ord_id
        ).filter(
            Market_Fact.ord_id.in_(ord_id)
        ).filter(
            Market_Fact.cust_id.in_(cust_id)
        ).subquery()
        
        logger.info("Getting customer id order id and order date as a subquery")
        
        subquery2 = sql.query(
            subquery1.c.cust_id,
            func.count(extract("Month", subquery1.c.order_date))
        ).group_by(
            subquery1.c.cust_id,
            extract("Month", subquery1.c.order_date)
        ).subquery()

        logger.info("Getting customer id and count of order id grouped by month")

        count = sql.query(
            func.count(subquery2.c.cust_id),
            subquery2.c.cust_id
        ).group_by(
            subquery2.c.cust_id
        ).all()

        logger.info("Getting Customer Id and number of months he/she has purchased in the given time")
        try:
            result = list()
            for i in range(len(count)):
                if count[i][0] > 12:
                    result.append(count[i][1])
            if len(result) ==0 :
                return "No customer found to satisfy the condition"
            return result
        except HTTPException as e:
            logger.error("No customer found to satisfy the condition")
    except HTTPException as e:
        logging.error("No orders found in the given order")
