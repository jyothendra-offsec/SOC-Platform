from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import (
    create_user,
    get_user_by_email,
    get_user_by_username,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    if get_user_by_username(db, user.username):
        raise HTTPException(
            status_code=400,
            detail="Username already exists",
        )

    if get_user_by_email(db, user.email):
        raise HTTPException(
            status_code=400,
            detail="Email already exists",
        )

    return create_user(db, user)
