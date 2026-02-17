from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from helpers.config import get_settings
# from controllers import DataController
from controllers.DataController import DataController
from controllers import ProjectController
import os
import aiofiles
from models import ResponseStatus 

data_router = APIRouter(
    prefix="/data",
    tags=["data"]
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile, app_settings = Depends(get_settings)):
    is_valid, signal = DataController().validate_file(file=file)
    if not is_valid:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": signal})
    
    
    projetct_dir_path = ProjectController().get_project_path(project_id=project_id)
    file_path = os.path.join(projetct_dir_path, file.filename)
    
    async with aiofiles.open(file_path, "wb") as f: 
        while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
            await f.write(chunk)
    return {"signal": ResponseStatus.FILE_UPLOAD_SUCCESS.value, "file_name": file.filename, "project_id": project_id}
    