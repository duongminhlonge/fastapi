from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True


class UserCreateSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
