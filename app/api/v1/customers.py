from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserSchema
from app.services.user_service import get_users
from app.core.database import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=list[UserSchema])
def read_users(db: Session = Depends(get_db)):
    return get_users(db)
