from fastapi import FastAPI
from app.api.router import router

app = FastAPI(title="My API")
app.include_router(router, prefix="/api")