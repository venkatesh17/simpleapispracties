from fastapi import APIRouter, HTTPException, status
from typing import List

from app.schemas.user import UserCreate, UserUpdate, UserResponse
from app.services.user_service import UserService

router = APIRouter()

@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_user(user: UserCreate):
    return UserService.create(user)


@router.get(
    "/",
    response_model=List[UserResponse]
)
def get_users():
    return UserService.get_all()


@router.get(
    "/{user_id}",
    response_model=UserResponse
)
def get_user(user_id: int):
    user = UserService.get_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user


@router.put(
    "/{user_id}",
    response_model=UserResponse,
    response_model_exclude_none=True
)
def update_user(user_id: int, user: UserUpdate):
    updated = UserService.update(user_id, user)
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return updated


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_user(user_id: int):
    success = UserService.delete(user_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
