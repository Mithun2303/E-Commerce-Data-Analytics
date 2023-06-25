from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import Json
from crud.customer import get_details,get_unique_customer
from fastapi import HTTPException


router=APIRouter()

@router.get("/customer/{id}",status_code=200)
def customer_details(id:str):
    response = get_details(id)
    if response == "Customer have zero order":
        raise HTTPException(status_code=204,detail="User have zero order")
    if response == "Customer Not Found":
        raise HTTPException(status_code=404,detail="User not found")
    else:
        response = jsonable_encoder(response)
        return JSONResponse(content=response)


@router.get("/unique/customer")
def unique():
    response = get_unique_customer()
    print(response)
    if response == "No order found":
        raise HTTPException(status_code=204,detail="No orders found in 2011")
    if response == "No customer found to satisfy the condition":
        raise HTTPException(status_code=204,detail="No customer found to satisfy the condition")
    else:
        response = jsonable_encoder(response)
        return JSONResponse(content=response)