import time

from clients.http.client import HTTPClient
from httpx import Response
from typing import TypedDict

from clients.http.gateway.client import build_gateway_client
from pydantic_create_user import UserSchema, GetUserResponseSchema, CreateUserRequestSchema


class CreateUserResponseDict(TypedDict):
    """
    Описание структуры ответа создания пользователя
    """
    user: UserSchema


class UsersGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/users сервиса http-gateway
    """

    def get_user_api(self, user_id: str) -> Response:
        """
        Получить данные пользователя по его user_id

        :param user_id: Идентификатор пользователя
        :return: Ответ от сервера (объект httpx.Response)
        """
        return self.get(f"/api/v1/users/{user_id}")

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Создание нового пользователя

        :param request: Словарь с данными нового пользователя
        :return: Ответ от сервера (объект httpx.Response)
        """
        return self.post("/api/v1/users", json=request)

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        response = self.get_user_api(user_id)
        return response.json()

    def create_user(self) -> CreateUserResponseDict:
        request = CreateUserRequestSchema(
            email=f"user.{time.time()}@example.com",
            lastName="string",
            firstName="string",
            middleName="string",
            phoneNumber="string",
        )
        response = self.create_user_api(request)
        return response.json()


def build_users_gateway_http_client() -> UsersGatewayHTTPClient:
    """
    Функция создает экземпляр UsersGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию UsersGatewayHTTPClient.
    """
    return UsersGatewayHTTPClient(client=build_gateway_client())
