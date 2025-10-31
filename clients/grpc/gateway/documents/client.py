from clients.grpc.client import GRPCClient
from grpc import Channel

from clients.grpc.gateway.client import build_gateway_grpc_client
from contracts.services.gateway.documents.documents_gateway_service_pb2_grpc import DocumentsGatewayServiceStub
from contracts.services.gateway.documents.rpc_get_tariff_document_pb2 import (
    GetTariffDocumentRequest,
    GetTariffDocumentResponse
)
from contracts.services.gateway.documents.rpc_get_contract_document_pb2 import (
    GetContractDocumentRequest,
    GetContractDocumentResponse
)
from tools.fakers import fake


class DocumentsGatewayGRPCClient(GRPCClient):
    """
    gRPC-клиент для взаимодействия с DocumentsGatewayService.
    Предоставляет высокоуровневые методы для получения данных о тарифах и контрактах.
    """

    def __init__(self, channel: Channel):
        """
        Инициализация клиента с указанным gRPC-каналом.

        :param channel: gRPC-канал для подключения к DocumentsGatewayService.
        """
        super().__init__(channel)

        self.stub = DocumentsGatewayServiceStub(channel)

    def get_tariff_document_api(self, request: GetTariffDocumentRequest) -> GetTariffDocumentResponse:
        """
        Низкоуровневый вызов метода GetTariffDocument через gRPC.

        :param request: gRPC-запрос с ID счета.
        :return: Ответ от сервиса с документами по тарифу.
        """
        return self.stub.GetTariffDocument(request)

    def get_contract_document_api(self, request: GetContractDocumentRequest) -> GetContractDocumentResponse:
        """
        Низкоуровневый вызов метода GetUser через gRPC.

        :param request: gRPC-запрос с ID счета.
        :return: Ответ от сервиса с документами по контракту.
        """
        return self.stub.GetContractDocument(request)

    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponse:
        """
        Получение документов по тарифу.

        :param account_id: Идентификатор счета.
        :return: Ответ с информацией о тарифах счета.
        """
        request = GetTariffDocumentRequest(account_id=account_id)
        return self.get_tariff_document_api(request)

    def get_contract_document(self, account_id: str) -> GetTariffDocumentResponse:
        """
        Получение документов по контракту.

        :param account_id: Идентификатор счета.
        :return: Ответ с информацией о документах счета.
        """
        request = GetContractDocumentRequest(account_id=account_id)
        return self.get_contract_document_api(request)


def build_documents_gateway_grpc_client() -> DocumentsGatewayGRPCClient:
    """
    Фабрика для создания экземпляра DocumentsGatewayGRPCClient.

    :return: Инициализированный клиент для DocumentsGatewayService.
    """
    return DocumentsGatewayGRPCClient(channel=build_gateway_grpc_client())
