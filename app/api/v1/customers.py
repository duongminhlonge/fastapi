from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserSchema
from app.services.user_service import get_users, get_user_by_id
from app.core.database import get_db
from fastapi import HTTPException

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=list[UserSchema])
def read_users(db: Session = Depends(get_db)):
    return get_users(db)


@router.get("/{user_id}", response_model=UserSchema)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
