from clients.http.client import HTTPClient
from httpx import Response, QueryParams, Client
from typing import TypedDict


class GetAccountQueryDict(TypedDict):
    """
    Структура данных для получения списка счетов пользователя
    """
    usrId: str


class OpenDepositAccountRequestDict(TypedDict):
    """
    Структура данных для открытия депозитного счета
    """
    usrId: str


class OpenSavingsAccountRequestDict(TypedDict):
    """
    Структура данных для открытия сберегательного счета
    """
    usrId: str


class OpenDebitCardRequestDict(TypedDict):
    """
    Структура данных для открытия дебетового счета
    """
    usrId: str


class OpenCreditCardRequestDict(TypedDict):
    """
    Структура данных для открытия кредитного счета
    """
    usrId: str


class AccountsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/accounts сервиса http-gateway
    """

    def get_accounts_api(self, query: GetAccountQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение списка счетов пользователя

        :param query: Словарь с параметрами запроса, например: {'useID': '123'}
        :return: Ответ от сервера (объект httpx.Response) с результатом операции
        """
        return self.get("/api/v1/accounts", params=QueryParams(**query))

    def open_deposit_account_api(self, request: OpenDepositAccountRequestDict) -> Response:
        """
        Выполняет POST-запрос для открытия депозитного счета

        :param request: Словарь с userId
        :return: Ответ от сервера (объект httpx.Response) с результатом операции
        """
        return self.post("/api/v1/accounts/open-deposit-account", json=request)

    def open_savings_account_api(self, request: OpenSavingsAccountRequestDict) -> Response:
        """
        Выполняет POST-запрос для открытия сберегательного счета

        :param request: Словарь с userId
        :return: Ответ от сервера (объект httpx.Response) с результатом операции
        """
        return self.post("/api/v1/accounts/open-savings-account", json=request)

    def open_debit_card_account_api(self, request: OpenDebitCardRequestDict) -> Response:
        """
        Выполняет POST-запрос для открытия дебетовой карты

        :param request: Словарь с userId
        :return: Ответ от сервера (объект httpx.Response) с результатом операции
        """
        return self.post("/api/v1/accounts/open-debit-card-account", json=request)

    def open_credit_card_account_api(self, request: OpenCreditCardRequestDict) -> Response:
        """
        Выполняет POST-запрос для открытия кредитной карты

        :param request: Словарь с userId
        :return: Ответ от сервера (объект httpx.Response) с результатом операции
        """
        return self.post("/api/v1/accounts/open-credit-card-account", json=request)

accounts_client = AccountsGatewayHTTPClient(client=Client(base_url="http://localhost:8003"))