from pydantic import BaseModel

class product(BaseModel):
    product_category:str
    product_sub_category:str
    product_id:str
    def __str__(self):
        return f"""
            "Category":{self.product_category},
            "sub_category":{self.product_sub_category},
            "Id":{self.product_id}
        """