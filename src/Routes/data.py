from fastapi import FastAPI, APIRouter, Depends, UploadFile 
from helpers.config import get_settings
# from controllers import DataController
from controllers.DataController import DataController


data_router = APIRouter(
    prefix="/data",
    tags=["data"]
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile, app_settings = Depends(get_settings)):
    is_valid, signal = DataController().validate_file(file=file)
    return {"   is_valid": is_valid, "signal": signal}