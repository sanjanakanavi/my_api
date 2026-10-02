from fastapi import APIRouter
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user

router = APIRouter()


@router.post("/", response_model=UserResponse)
def create_user_endpoint(user: UserCreate):
    return create_user(user)