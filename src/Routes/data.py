from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from helpers.config import get_settings
# from controllers import DataController
from controllers.DataController import DataController
from controllers import ProjectController , ProcessController
import os
import aiofiles
from models import ResponseStatus 
from .schemes.data import ProcessRequest
import logging

logger = logging.getLogger("uvicorn.error")

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
    file_path, file_id = DataController().generate_unique_filepath(original_filename=file.filename, project_id=project_id)
    try:
        async with aiofiles.open(file_path, "wb") as f: 
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:
            logging.error(f"Error uploading file: {e}")
            return JSONResponse(status_code=ResponseStatus.FILE_UPLOAD_FAILED.value, content={"message": signal})

    return {"signal": ResponseStatus.FILE_UPLOAD_SUCCESS.value, "file_name": file.filename, "project_id": project_id , "file_id": file_id}
    


@data_router.post("/process/{project_id}")
async def process_endpoint(project_id: str, request: ProcessRequest):
    file_id = request.file_id
    chunk_size = request.chunk_size
    chunk_overlap = request.chunk_overlap
    
    process_controller = ProcessController(project_id=project_id)
    file_content = process_controller.get_file_content(file_id=file_id)
    chunks = process_controller.process_file_content(file_content=file_content,file_id=file_id,chunk_size=chunk_size,chunk_overlap=chunk_overlap)
    return chunks

