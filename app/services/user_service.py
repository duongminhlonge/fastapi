from sqlalchemy.orm import Session
from app.models.user import User


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

    new_user = User(
        username=user_data.username, email=user_data.email, password=user_data.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
