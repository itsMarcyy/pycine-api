from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    id_: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True


class UserResponse(BaseModel):
    id_: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        from_attributes = True