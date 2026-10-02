# app/schemas/response.py
from typing import Any
from pydantic import BaseModel



class ApiResponse(BaseModel):
    status_code: int
    message: str
    data: Any = None