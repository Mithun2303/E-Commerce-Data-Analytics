from fastapi import APIRouter
from crud.get_sales import get_profit
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import Json
from fastapi import HTTPException


router = APIRouter(prefix="/profit")

@router.get("",response_model = Json,status_code = 200)
def profit():
    response = get_profit()
    if response == "No sale was done":
        raise HTTPException(status_code=204,detail=response)
    else:
        response=jsonable_encoder(response)
        return JSONResponse(content=response)