from app.schemas.ApiResponse import ApiResponse
from app.schemas.user import UserCreate


def create_user(user: UserCreate) -> ApiResponse:
    # Put business rules here. Replace this example with database access later.
    # return ApiResponse(
    #     status_code=201,
    #     message="User created successfully",
    #     data={"id": 1, "name": user.name, "email": user.email},
    # )

    return ApiResponse(
            status_code=404,
            message="User not found",
            data=None
        )
