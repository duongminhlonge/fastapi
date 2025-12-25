from pydantic import BaseModel, EmailStr, constr


class UserSchema(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True


class UserCreateSchema(BaseModel):
    username: str
    email: EmailStr
    password: constr(min_length=8, max_length=72)
