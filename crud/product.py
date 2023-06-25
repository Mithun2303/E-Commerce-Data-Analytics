from database import SessionClass
from schemas.product_dimension import Product_Dimension
import logging

logger = logging.getLogger(__name__)

sql1 = SessionClass()
sql = sql1.get_session()


def get_product_details(product_category:str):
    product_category=product_category.upper()
    try:
        query=sql.query(Product_Dimension).filter(Product_Dimension.product_category==product_category).all()
        logger.info(f"Getting product category details:{product_category}")
        if not query:
            logger.error("Category not found")
            return "Product category not found"    
        else:
            logger.info(f"Product category exists {product_category}")
            return query
    except Exception as e:
        logger.error("Product category not found")


