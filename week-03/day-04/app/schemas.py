from pydantic import BaseModel, Field, field_validator, EmailStr, ConfigDict

class UserCreate(BaseModel):
    username: str
    email: EmailStr


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    priority: int = Field(ge=1, le=5)

    @field_validator("title")
    @classmethod
    def title_must_not_be_blank(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("Title cannot be blank")

        return value


class TaskUpdate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    priority: int = Field(ge=1, le=5)

    @field_validator("title")
    @classmethod
    def title_must_not_be_blank(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("Title cannot be blank")

        return value

class TaskResponse(BaseModel):
    id: int
    title: str
    priority: int
    status: str
    user_id: int

    model_config = ConfigDict(from_attributes=True)