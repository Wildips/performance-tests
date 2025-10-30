from clients.http.client import HTTPClient
from httpx import Response, QueryParams, request
from typing import TypedDict

from clients.http.gateway.client import build_gateway_client


class OperationDict(TypedDict):
    """
    Описание структуры операции
    """
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str


class OperationReceiptDict(TypedDict):
    """
    Описание структуры квитанции
    """
    url: str
    document: str


class OperationSummaryDict(TypedDict):
    """
    Описания структуры сумморизации
    """
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float


class GetOperationReceiptResponseDict(TypedDict):
    """
    Описание структуры ответа получения квитанции
    """
    receipt: OperationReceiptDict


class GetOperationsResponseDict(TypedDict):
    """
    Описание структуры ответа по операциям
    """
    operations: list[OperationDict]


class GetOperationsSummaryResponseDict(TypedDict):
    """
    Описание структуры ответа по операции суммаризации
    """
    summary: OperationSummaryDict


class GetOperationResponseDict(TypedDict):
    """
    Описание структуры ответа по операции
    """
    operation: OperationDict


class GetOperationsQueryDict(TypedDict):
    """
    Структура данных для получения списка операций по счету
    """
    accountId: str


class GetOperationsSummaryQueryDict(TypedDict):
    """
    Структура данных для получения итоговых данных по счету
    """
    accountId: str


class MakeFeeOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции с комиссией
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeFeeOperationResponseDict(TypedDict):
    """
    Описание структуры ответа по операции комиссии
    """
    operation: OperationDict


class MakeTopUpOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции пополнения счета
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeTopUpOperationResponseDict(TypedDict):
    """
    Описание структуры ответа по операции пополнения
    """
    operation: OperationDict


class MakeCashbackOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции кэшбэка
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeCashbackOperationResponseDict(TypedDict):
    """
    Описание структуры ответа по операции кэшбэка
    """
    operation: OperationDict


class MakeTransferOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции перевода средств
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeTransferOperationResponseDict(TypedDict):
    """
    Описание структуры ответа по операции перевода средств
    """
    operation: OperationDict


class MakePurchaseOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции списания средств
    """
    status: str
    amount: float
    cardId: str
    accountId: str
    category: str


class MakePurchaseOperationResponseDict(TypedDict):
    """
    Описание структуры ответа по операции списания средств
    """
    operation: OperationDict


class MakeBillPaymentOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции оплаты по счету
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeBillPaymentOperationResponseDict(TypedDict):
    """
    Описание структуры ответа по операции оплаты по счету
    """
    operation: OperationDict


class MakeCashWithdrawalOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции снятия средств
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeCashWithdrawalOperationResponseDict(TypedDict):
    """
    Описание структуры ответа по снятия средств
    """
    operation: OperationDict


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway
    """

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение списка операций счета

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}
        :return: Ответ от сервера (объект httpx.Response) с результатом операции
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение итоговых данных по операциям счета

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}
        :return: Ответ от сервера (объект httpx.Response) с результатом операции
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query))

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получение документов по операции

        :param operation_id: Идентификатор операции
        :return: Ответ от сервера (объект httpx.Response) с результатом операции
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получение данных по операции

        :param operation_id: Идентификатор операции
        :return: Ответ от сервера (объект httpx.Response) с результатом операции
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Создание операции с комиссией

        :param request: Словарь с данными операции с комиссией
        :return: Ответ от сервера (объект httpx.Response)
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Создание операции пополнения счета

        :param request: Словарь с данными операции пополнения счета
        :return: Ответ от сервера (объект httpx.Response)
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Создание операции кэшбэка

        :param request: Словарь с данными операции кэшбэка
        :return: Ответ от сервера (объект httpx.Response)
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Создание операции перевода средств

        :param request: Словарь с данными операции перевода средств
        :return: Ответ от сервера (объект httpx.Response)
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Создание операции списания средств

        :param request: Словарь с данными операции списания средств
        :return: Ответ от сервера (объект httpx.Response)
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Создание операции оплаты по счету

        :param request: Словарь с данными операции оплаты по счету
        :return: Ответ от сервера (объект httpx.Response)
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Создание операции оплаты снятия средств

        :param request: Словарь с данными операции снятия средств
        :return: Ответ от сервера (объект httpx.Response)
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        query = GetOperationsSummaryQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        response = self.get_operation_receipt_api(operation_id)
        return response.json()

    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        response = self.get_operation_api(operation_id)
        return response.json()

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseDict:
        request = MakeFeeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseDict:
        request = MakeTopUpOperationRequestDict(
            status="COMPLETED",
            amount=1500,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseDict:
        request = MakeCashbackOperationRequestDict(
            status="COMPLETED",
            amount=100,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseDict:
        request = MakeTransferOperationRequestDict(
            status="COMPLETED",
            amount=200,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseDict:
        request = MakePurchaseOperationRequestDict(
            status="COMPLETED",
            amount=500,
            cardId=card_id,
            accountId=account_id,
            category="taxi"
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseDict:
        request = MakeBillPaymentOperationRequestDict(
            status="COMPLETED",
            amount=200,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseDict:
        request = MakeCashWithdrawalOperationRequestDict(
            status="COMPLETED",
            amount=750,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создает экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_client())
