from app.schemas.user import UserCreate


def create_user(user: UserCreate) -> dict:
    # Put business rules here. Replace this example with database access later.
    return {"id": 1, "name": user.name, "email": user.email}