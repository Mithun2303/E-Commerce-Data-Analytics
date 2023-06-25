from database import SessionClass
from schemas.market_fact import Market_Fact
from schemas.customer_dimension import Customer_Dimension
from schemas.order_dimension import Order_Dimension
from schemas.product_dimension import Product_Dimension
from schemas.shipping_dimension import Shipping_Dimension
from models.order import orders
from models.get_order import Get_Orders
from models.product import product
from models.shipping import Shipping
from models.custorder import Custorder
from datetime import date
import logging

logger = logging.getLogger(__name__)

sql1 = SessionClass()
sql = sql1.get_session()

def get_details(id:str):
    id=id.capitalize()
    try:    
        order_exist=sql.query(
                Market_Fact,
                Product_Dimension,
                Shipping_Dimension,
                Order_Dimension,
                ).join(
                Product_Dimension
                ).join(
                Order_Dimension
                ).join(
                Shipping_Dimension
                ).filter(
                Market_Fact.ord_id==id
                ).first()
        logger.info("Getting the order details")
        try:
            count_order = sql.query(
                    Market_Fact
                ).filter(
                    Market_Fact.cust_id == order_exist.Market_Fact.cust_id
                ).count()
            logger.info("Getting the number of orders the customer ordered")
        except AttributeError as e:
            logger.error("Order does not exist")
            return "Order Does Not Exist"
        try:
            cust_details = sql.query(
                    Customer_Dimension
                ).filter(
                    Customer_Dimension.customer_id == order_exist.Market_Fact.cust_id
                ).first()
        except AttributeError as e:
            error = str(e)
            return error
    except AttributeError as e:
        error = str(e)
        return error
    ord_date = order_exist.Order_Dimension.order_date
    ship_date = order_exist.Shipping_Dimension.shipping_date
    diff=(((ship_date-ord_date).days))
    order_details = Get_Orders(
        cust = Custorder(
            cust_name = cust_details.customer_name,
            cust_id = cust_details.customer_id,
            cust_province = cust_details.province,
            cust_region = cust_details.region,
            no_of_order = count_order
            ),
        order = orders(
            order_id = order_exist.Order_Dimension.ord_id,
            order_date = str(order_exist.Order_Dimension.order_date),
            order_priority = order_exist.Order_Dimension.order_priority
            ),
        ship = Shipping(
            mode = order_exist.Shipping_Dimension.shipping_mode,
            date = str(order_exist.Shipping_Dimension.shipping_date),
            id = order_exist.Shipping_Dimension.shipping_id
            ),
        prod = product(
            product_category = order_exist.Product_Dimension.product_category,
            product_sub_category = order_exist.Product_Dimension.product_sub_category,
            product_id = order_exist.Product_Dimension.product_id
            ),
        delivered_in = diff
        )

    return order_details
