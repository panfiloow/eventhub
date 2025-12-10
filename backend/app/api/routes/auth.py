from fastapi import APIRouter, status

from app.api.deps import UserDep
from app.schemas.user import UserCreate, UserResponse

router = APIRouter()


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
)
async def register(user_in: UserCreate, user_service: UserDep) -> UserResponse:
    """
    Регистрация нового пользователя.
    """
    return await user_service.register_user(user_in)
