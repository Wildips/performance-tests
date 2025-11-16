from pydantic import BaseModel, HttpUrl


class TariffSchema(BaseModel):
    """
    Структура данных для перечня документов по тарифу
    """
    url: HttpUrl
    document: str


class GetTariffDocumentResponseSchema(BaseModel):
    """
    Описание структуры ответа получения информации по тарифу
    """
    tariff: TariffSchema


class ContractSchema(BaseModel):
    """
    Структура данных для перечня документов по контракту
    """
    url: HttpUrl
    document: str


class GetContractDocumentResponseSchema(BaseModel):
    """
    Описание структуры ответа получения информации по контракту
    """
    contract: ContractSchema
