import random

from pydantic import BaseModel, Field


class SeedCardResult(BaseModel):
    """
    Результат генерации карты.

    Attributes:
        card_id (str): Уникальный идентификатор карты.
    """
    card_id: str


class SeedOperationResult(BaseModel):
    """
    Результат генерации операции.

    Attributes:
        operation_id (str): Уникальный идентификатор операции.
    """
    operation_id: str


class SeedAccountResult(BaseModel):
    """
    Результат генерации счета с вложенными сущностями.

    Attributes:
        account_id (str): Уникальный идентификатор счета.
        physical_card (list[SeedCardResult]): Список физических карт, привязанных к счету.
        top_up_operations (list[SeedOperationResult]): Список операций пополнения.
        purchase_operations (list[SeedOperationResult]): Список операций покупки.
    """
    account_id: str
    physical_card: list[SeedCardResult] = Field(default_factory=list)
    top_up_operations: list[SeedOperationResult] = Field(default_factory=list)
    purchase_operations: list[SeedOperationResult] = Field(default_factory=list)


class SeedUserResult(BaseModel):
    """
    Результат генерации пользователей с привязанными счетами.

    Attributes:
        user_id (str): Уникальный идентификатор пользователя.
        deposit_accounts (list[SeedAccountResult]): Список депозитных счетов.
        savings_accounts (list[SeedAccountResult]): Список сберегательных счетов.
        debit_card_accounts (list[SeedAccountResult]): Список дебетовых счетов.
        credit_card_accounts (list[SeedAccountResult]): Список кредитных счетов.
    """
    user_id: str
    deposit_accounts: list[SeedAccountResult] = Field(default_factory=list)
    savings_accounts: list[SeedAccountResult] = Field(default_factory=list)
    debit_card_accounts: list[SeedAccountResult] = Field(default_factory=list)
    credit_card_accounts: list[SeedAccountResult] = Field(default_factory=list)


class SeedsResult(BaseModel):
    """
    Главная модель результата сиднга - агрегирует всех созданных пользователей.

    Attributes:
        users (list[SeedUserResult]): Список сгенерированных пользователй.
    """
    users: list[SeedUserResult] = Field(default_factory=list)

    def get_next_user(self) -> SeedUserResult:
        """
        Возвращает и удаляет первого пользователя из списка.

        Используется в случае, когда для каждого виртуального юзера нужен тестовый пользователь.
        Удобно при строго последовательной раздаче пользователей в тестовых сценариях.

        :return: SeedUserResult: Случайный пользователь из списка.
        """
        return self.users.pop(0)

    def get_random_user(self):
        """
        Возвращает случайного пользователя из списка без удаления.

        Используется в ситуациях, когда порядок не имеет значения, и пользователь выбирается случайно.

        :return: SeedUserResult: Случайный пользователь из списка.
        """
        return random.choice(self.users)
