from pydantic import BaseModel, ConfigDict, EmailStr, Field
from pydantic.alias_generators import to_camel

from tools.fakers import fake

class UserSchema(BaseModel):
    """
    Описание структуры пользователя
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")


class CreateUserRequestSchema(BaseModel):
    """
    Структура данных для создания нового пользователя
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    email: EmailStr = Field(default_factory=fake.email)
    last_name: str = Field(alias="lastName", default_factory=fake.last_name)
    first_name: str = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: str = Field(alias="middleName", default_factory=fake.middle_name)
    phone_number: str = Field(alias="phoneNumber", default_factory=fake.phone_number)


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа при создании пользователя
    """
    user: UserSchema


class GetUserResponseSchema(BaseModel):
    """
    Описание структуры ответа получения данных пользователя
    """
    user: UserSchema
