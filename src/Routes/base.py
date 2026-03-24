from fastapi import FastAPI, APIRouter, Depends
from helpers.config import get_settings

base_router = APIRouter(
    prefix="/base",
    tags=["base"]
)


@base_router.get("/")
def welcome(app_settings = Depends(get_settings)):
    
    app_name = app_settings.App_Name
    app_version = app_settings.App_Version 
    return {"app_name": app_name, "app_version": app_version, "message": "Welcome to the MINI_RAG API!"}