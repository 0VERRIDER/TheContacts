from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(..., min_length=3)
    phone: str = Field(..., regex=r'^\+?1?\d{9,15}$')
    password: str = Field(..., min_length=8)
    email: str = Field(None, regex=r'^[\w-]+@([\w-]+\.)+[\w-]+$')

class UserInDB(User):
    id: str

class UserCreate(User):
    pass