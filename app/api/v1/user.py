from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.schemas.user import UserSchema, UserCreateSchema
from app.services.user_service import (
    get_users,
    get_user_by_id,
    create_user,
    authenticate_user,
)
from app.db.base import get_db
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user import TokenSchema
from app.core.security import create_access_token
from app.dependencies.auth import get_current_user


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserSchema)
def read_me(current_user=Depends(get_current_user)):
    return current_user


@router.get("/", response_model=list[UserSchema])
def read_users(db: Session = Depends(get_db)):
    return get_users(db)


@router.get("/{user_id}", response_model=UserSchema)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# Create a new user
@router.post("/", response_model=UserSchema, name="create_user")
def create_user_endpoint(user: UserCreateSchema, db: Session = Depends(get_db)):
    new_user = create_user(db, user)
    if not new_user:
        raise HTTPException(status_code=400, detail="Username or email already exists")
    return new_user


@router.post("/login", response_model=TokenSchema)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
