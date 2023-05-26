from fastapi import APIRouter

router = APIRouter()


@router.get("/users/")
def read_users():
    return [{"user_id": "1", "username": "John Doe"}]
