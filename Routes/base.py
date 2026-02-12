from fastapi import FastAPI, APIRouter
import os

base_router = APIRouter(
    prefix="/base",
    tags=["base"]
)


@base_router.get("/")
def welcome():
    app_name = os.getenv("APP_NAME", "FastAPI Application")
    return {"message": "Welcome to all!"}