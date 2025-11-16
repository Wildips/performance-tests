from locust.env import Environment
from httpx import Response

from clients.http.client import HTTPClient, HTTPClientExtensions
from clients.http.gateway.client import build_gateway_http_client, build_gateway_locust_http_client
from clients.http.gateway.users.schema import (
    GetUserResponseSchema,
    CreateUserRequestSchema,
    CreateUserResponseSchema)
from tools.routes import APIRoutes


class UsersGatewayHTTPClient(HTTPClient):
    f"""
    Клиент для взаимодействия с {APIRoutes.USERS} сервиса http-gateway
    """

    def get_user_api(self, user_id: str) -> Response:
        """
        Получить данные пользователя по его user_id

        :param user_id: Идентификатор пользователя
        :return: Ответ от сервера (объект httpx.Response)
        """
        return self.get(
            url=f"{APIRoutes.USERS}{user_id}",
            extensions=HTTPClientExtensions(route=f"{APIRoutes.USERS}{{user_id}}")
        )

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Создание нового пользователя

        :param request: Словарь с данными нового пользователя
        :return: Ответ от сервера (объект httpx.Response)
        """
        return self.post(f"{APIRoutes.USERS}", json=request.model_dump(by_alias=True))

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)

    def create_user(self) -> CreateUserResponseSchema:
        request = CreateUserRequestSchema()
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def build_users_gateway_http_client() -> UsersGatewayHTTPClient:
    """
    Функция создает экземпляр UsersGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию UsersGatewayHTTPClient.
    """
    return UsersGatewayHTTPClient(client=build_gateway_http_client())


def build_users_gateway_locust_http_client(environment: Environment) -> UsersGatewayHTTPClient:
    """
    Функция создает экземпляр UsersGatewayHTTPClient адаптированный под Locust.

    Клиент автоматически собирает метрики и передает их в Locust через хуки.
    Используется исключительно в нагрузочных тестах

    :param environment: объект окружения Locust
    :return: Экземпляр UsersGatewayHTTPClient с хуком сбора метрик.
    """
    return UsersGatewayHTTPClient(client=build_gateway_locust_http_client(environment=environment))
