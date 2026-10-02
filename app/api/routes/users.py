from fastapi import APIRouter, Response
from app.schemas.ApiResponse import ApiResponse
from app.schemas.user import UserCreate
from app.services.user_service import create_user

router = APIRouter()


@router.post("/", response_model=ApiResponse)
def create_user_endpoint(user: UserCreate):
    print("create_user_endpoint called with user:", user)  
    return create_user(user)

@router.post("/getuser", response_model=ApiResponse)
def get_user_endpoint(user: UserCreate):
    print("get_user_endpoint called with user:", user)  
    return create_user(user)