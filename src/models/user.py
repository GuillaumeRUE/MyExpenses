from sqlmodel import SQLModel, Field


class UserBase(SQLModel):
    email: str
    is_active: bool = True


class UserCreate(UserBase):
    password: str


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str
