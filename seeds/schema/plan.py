from pydantic import BaseModel, Field


class SeedACardsPlan(BaseModel):
    """
    План генерации карт на счете.

    Attributes: count (int): Количество карт (виртуальных или физических), которые нужно создать.
    """
    count: int = 0


class SeedOperationsPlan(BaseModel):
    """
    План генерации операций на счете.

    Attributes: count (int): Количество операций (например, пополнений или покупок), которые нужно сгенерировать.
    """
    count: int = 0


class SeedAccountsPlan(BaseModel):
    """
    План генерации счетов одного типа (например, депозитных или кредитных).

    Attributes:
        count (int): Количество счетов данного типа.
        physical_card (SeedACardsPlan): План по созданию физических карт на счетах.
        top_up_operations (SeedOperationsPlan): План по созданию операций пополнения.
        purchase_operations (SeedOperationsPlan): План по созданию операций покупки.
    """
    count: int = 0
    physical_card: SeedACardsPlan = Field(default_factory=SeedACardsPlan)
    top_up_operations: SeedOperationsPlan = Field(default_factory=SeedOperationsPlan)
    purchase_operations: SeedOperationsPlan = Field(default_factory=SeedOperationsPlan)


class SeedUsersPlan(BaseModel):
    """
    План по созданию пользователей и их счетов разных типов.

    Attributes:
        count (int): Количество пользователей.
        deposit_accounts (SeedAccountsPlan): План по депозитным счетам.
        savings_accounts (SeedAccountsPlan): План по сберегательным счетам.
        debit_card_accounts (SeedAccountsPlan): План по дебетовым картам.
        credit_card_accounts (SeedAccountsPlan): План по кредитным картам.
    """
    count: int = 0
    deposit_accounts: SeedAccountsPlan = Field(default_factory=SeedAccountsPlan)
    savings_accounts: SeedAccountsPlan = Field(default_factory=SeedAccountsPlan)
    debit_card_accounts: SeedAccountsPlan = Field(default_factory=SeedAccountsPlan)
    credit_card_accounts: SeedAccountsPlan = Field(default_factory=SeedAccountsPlan)


class SeedsPlan(BaseModel):
    """
    Главная модель пана сидинга.

    Attributes:
        users (SeedUsersPlan): План по созданию пользователей и всей связанно структуры.
    """
    users: SeedUsersPlan = Field(default_factory=SeedUsersPlan)
