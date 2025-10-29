from clients.http.client import HTTPClient
from httpx import Response, Client


class DocumentsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/documents сервиса http-gateway
    """

    def get_tariff_document_api(self, account_id: str) -> Response:
        """
        Получение тарифа по счету

        :param account_id: Идентификатор счета
        :return: Ответ от сервера (объект httpx.Response) с результатом операции
        """
        return self.get(f"/api/v1/documents/tariff-document/{account_id}")

    def get_contract_document_api(self, account_id: str) -> Response:
        """
        Получение контракта по счету

        :param account_id: Идентификатор счета
        :return: Ответ от сервера (объект httpx.Response) с результатом операции
        """
        return self.get(f"/api/v1/documents/contract-document/{account_id}")


documents_client = DocumentsGatewayHTTPClient(client=Client(base_url="http://localhost:8003"))
