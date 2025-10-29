from clients.http.client import HTTPClient
from httpx import Response, Client
from typing import TypedDict


class CreateCardRequestDict(TypedDict):
    """
    Структура данных для создания нового пользователя
    """
    userId: str
    accountId: str


class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards сервиса http-gateway
    """

    def issue_virtual_card_api(self, request: CreateCardRequestDict) -> Response:
        """
        Создание виртуальной карты по user_id и account_id

        :param request: Словарь с данными виртуальной карты
        :return: Ответ от сервера (объект httpx.Response)
        """
        return self.post(f"/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: CreateCardRequestDict) -> Response:
        """
        Создание физической карты по user_id и account_id

        :param request: Словарь с данными физической карты
        :return: Ответ от сервера (объект httpx.Response)
        """
        return self.post("/api/v1/cards/issue-physical-card", json=request)


cards_client = CardsGatewayHTTPClient(client=Client(base_url="http://localhost:8003"))
