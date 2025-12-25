from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hash_password, verify_password


def get_users(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, user_data):
    # Check duplicate username/email
    existing_user = (
        db.query(User)
        .filter((User.username == user_data.username) | (User.email == user_data.email))
        .first()
    )
    if existing_user:
        return None  # API layer handles HTTPException

    hashed_pwd = hash_password(user_data.password)
    new_user = User(
        username=user_data.username, email=user_data.email, password=hashed_pwd
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()
