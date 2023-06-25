from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import Json
from models.market_fact import Market_Fact_Model
from fastapi import HTTPException
from crud.maxorders import get_max_order
router = APIRouter(prefix= "/maxorder")

@router.get("/{first}/{off_set}",status_code = 200,response_model = Json)
def getmax(first:int,off_set:int):
    response = get_max_order(first,off_set)
    if response == "Customer index out of range":
        raise HTTPException(status_code=204,detail="Customer index out of range")
    content = jsonable_encoder(response)
    return JSONResponse(content=content)
