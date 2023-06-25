from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
from pydantic import Json
from crud.product import get_product_details
router=APIRouter(prefix='/product')


@router.get('/details/{product_category}',status_code=200,response_model=Json)
def product_details(product_category:str):
    response = get_product_details(product_category)
    if response == "Product category not found":
        raise HTTPException(status_code=404,detail=response)
    response = jsonable_encoder(response)
    return   JSONResponse(content = response)
