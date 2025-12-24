from pydantic import BaseModel, Field

class UserBase(BaseModel):
    name: str
    username: str
    email: str
    website: str | None = None
    company_name: str | None = None

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int

    model_config = {"from_attributes": True}