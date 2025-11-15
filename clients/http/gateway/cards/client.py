from locust.env import Environment
from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.cards.schema import (
    IssueVirtualCardRequestSchema,
    IssuePhysicalCardRequestSchema,
    IssueVirtualCardResponseSchema,
    IssuePhysicalCardResponseSchema
)
from clients.http.gateway.client import build_gateway_http_client, build_gateway_locust_http_client
from tools.routes import APIRoutes


class CardsGatewayHTTPClient(HTTPClient):
    f"""
    Клиент для взаимодействия с {APIRoutes.CARDS} сервиса http-gateway
    """

    def issue_virtual_card_api(self, request: IssueVirtualCardRequestSchema) -> Response:
        """
        Создание виртуальной карты по user_id и account_id

        :param request: Словарь с данными виртуальной карты
        :return: Ответ от сервера (объект httpx.Response)
        """

        return self.post(f"{APIRoutes.USERS}/issue-virtual-card", json=request.model_dump(by_alias=True))

    def issue_physical_card_api(self, request: IssuePhysicalCardRequestSchema) -> Response:
        """
        Создание физической карты по user_id и account_id

        :param request: Словарь с данными физической карты
        :return: Ответ от сервера (объект httpx.Response)
        """
        return self.post(f"{APIRoutes.USERS}/issue-physical-card", json=request.model_dump(by_alias=True))

    def issue_virtual_card(self, user_id: str, account_id: str) -> IssueVirtualCardResponseSchema:
        request = IssueVirtualCardRequestSchema(
            user_id=user_id,
            account_id=account_id
        )
        response = self.issue_virtual_card_api(request)
        return IssueVirtualCardResponseSchema.model_validate_json(response.text)

    def issue_physical_card(self, user_id: str, account_id: str) -> IssuePhysicalCardResponseSchema:
        request = IssuePhysicalCardRequestSchema(
            user_id=user_id,
            account_id=account_id
        )
        response = self.issue_physical_card_api(request)
        return IssuePhysicalCardResponseSchema.model_validate_json(response.text)


def build_cards_gateway_http_client() -> CardsGatewayHTTPClient:
    """
    Функция создает экземпляр CardsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CardsGatewayHTTPClient.
    """
    return CardsGatewayHTTPClient(client=build_gateway_http_client())


def build_cards_gateway_locust_http_client(environment: Environment) -> CardsGatewayHTTPClient:
    """
    Функция создает экземпляр CardsGatewayHTTPClient адаптированный под Locust.

    Клиент автоматически собирает метрики и передает их в Locust через хуки.
    Используется исключительно в нагрузочных тестах

    :param environment: объект окружения Locust
    :return: Экземпляр CardsGatewayHTTPClient с хуком сбора метрик.
    """
    return CardsGatewayHTTPClient(client=build_gateway_locust_http_client(environment=environment))
