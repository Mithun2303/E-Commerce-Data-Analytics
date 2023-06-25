from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import Json
from crud.order import get_details
from fastapi import HTTPException
router = APIRouter(prefix="/order")

@router.get('/{id}', status_code = 201, response_model = Json)
def order_details(id:str):
    response = get_details(id)
    if response == "Order Does Not Exist":
        raise HTTPException(status_code=404,detail="Order does not exist")
    else:
        response = jsonable_encoder(response)
        return JSONResponse(content=response)