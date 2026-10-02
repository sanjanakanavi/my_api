from fastapi import APIRouter
from app.api.routes import products, users


# Register the routers for the different endpoints

router = APIRouter()
router.include_router(users.router, prefix="/users", tags=["users"])
# router.include_router(products.router, prefix="/products", tags=["products"])