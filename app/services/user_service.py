from typing import List, Optional
from app.schemas.user import UserCreate, UserUpdate

class UserService:
    _users: List[dict] = []
    _id_counter: int = 1

    @classmethod
    def create(cls, user: UserCreate) -> dict:
        new_user = {
            "id": cls._id_counter,
            "name": user.name,
            "email": user.email
        }
        cls._users.append(new_user)
        cls._id_counter += 1
        return new_user

    @classmethod
    def get_all(cls) -> List[dict]:
        return cls._users

    @classmethod
    def get_by_id(cls, user_id: int) -> Optional[dict]:
        return next((u for u in cls._users if u["id"] == user_id), None)

    @classmethod
    def update(cls, user_id: int, user: UserUpdate) -> Optional[dict]:
        db_user = cls.get_by_id(user_id)
        if not db_user:
            return None

        if user.name is not None:
            db_user["name"] = user.name
        if user.email is not None:
            db_user["email"] = user.email

        return db_user

    @classmethod
    def delete(cls, user_id: int) -> bool:
        user = cls.get_by_id(user_id)
        if not user:
            return False
        cls._users.remove(user)
        return True
