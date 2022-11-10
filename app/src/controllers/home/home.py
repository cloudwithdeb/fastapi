
from fastapi import APIRouter
from src.dto.response import ResponseModel
from fastapi.responses import JSONResponse
from src.services.home.home import homePageService

router = APIRouter()

@router.get("/", response_model=ResponseModel)
async def homePageController():
    
    try:
        _home = homePageService()
        return JSONResponse(content=_home, status_code=200)
    
    except:
        return JSONResponse(content={"data": None, "message": "error", "status": False}, status_code=500)

   