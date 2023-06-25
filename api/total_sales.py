from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import Json
from crud.get_sales import get_sales
from fastapi import HTTPException
router =APIRouter(prefix= "/sales")

@router.get("",response_model = Json,status_code = 200)
def sales():
    response = get_sales()
    if response == "No sale has been done":
        raise HTTPException(status_code=204,detail="No sale has been done")
    else:
        response=jsonable_encoder(response)
        return JSONResponse(content=response)
    
