from enum import StrEnum
from pydantic import BaseModel, ConfigDict, Field, HttpUrl
from pydantic.alias_generators import to_camel

from tools.fakers import fake


class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"


class OperationSchema(BaseModel):
    """
    Описание структуры операции
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")


class OperationReceiptSchema(BaseModel):
    """
    Описание структуры квитанции
    """
    url: HttpUrl
    document: str


class OperationSummarySchema(BaseModel):
    """
    Описания структуры сумморизации
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")


class GetOperationReceiptResponseSchema(BaseModel):
    """
    Описание структуры ответа получения квитанции
    """
    receipt: OperationReceiptSchema


class GetOperationsResponseSchema(BaseModel):
    """
    Описание структуры ответа по операциям
    """
    operations: list[OperationSchema]


class GetOperationsSummaryResponseSchema(BaseModel):
    """
    Описание структуры ответа по операции суммаризации
    """
    summary: OperationSummarySchema


class GetOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа по операции
    """
    operation: OperationSchema


class GetOperationsQuerySchema(BaseModel):
    """
    Структура данных для получения списка операций по счету
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    account_id: str = Field(alias="accountId")


class GetOperationsSummaryQuerySchema(BaseModel):
    """
    Структура данных для получения итоговых данных по счету
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    account_id: str = Field(alias="accountId")


class MakeFeeOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции с комиссией
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeFeeOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа по операции комиссии
    """
    operation: OperationSchema


class MakeTopUpOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции пополнения счета
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeTopUpOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа по операции пополнения
    """
    operation: OperationSchema


class MakeCashbackOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции кэшбэка
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeCashbackOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа по операции кэшбэка
    """
    operation: OperationSchema


class MakeTransferOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции перевода средств
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeTransferOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа по операции перевода средств
    """
    operation: OperationSchema


class MakePurchaseOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции списания средств
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")
    category: str = Field(default_factory=fake.category)


class MakePurchaseOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа по операции списания средств
    """
    operation: OperationSchema


class MakeBillPaymentOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции оплаты по счету
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeBillPaymentOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа по операции оплаты по счету
    """
    operation: OperationSchema


class MakeCashWithdrawalOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции снятия средств
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа по снятия средств
    """
    operation: OperationSchema
