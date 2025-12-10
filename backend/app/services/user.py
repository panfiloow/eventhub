from app.core.exceptions import UserAlreadyExistsException
from app.core.security import get_password_hash
from app.repositories.user import UserRepository
from app.schemas.user import UserCreate, UserResponse


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def register_user(self, user_in: UserCreate) -> UserResponse:
        """
        Регистрирует нового пользователя.
        """
        existing_user = await self.user_repo.get_by_email(user_in.email)
        if existing_user:
            raise UserAlreadyExistsException()

        hashed_password = get_password_hash(user_in.password)
        user_data = user_in.model_dump(exclude={"password"})
        user_data["hashed_password"] = hashed_password
        user_data["is_active"] = True
        user_data["is_superuser"] = False

        new_user = await self.user_repo.create(user_data)

        return UserResponse.model_validate(new_user)
