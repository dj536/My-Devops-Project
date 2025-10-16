# lab/src/app.py
from fastapi import FastAPI
from .routes import user as user_router

app = FastAPI()
app.include_router(user_router.router, prefix="/user")