from clients.grpc.gateway.users.client import UsersGatewayGRPCClient, build_users_gateway_grpc_client
from clients.grpc.gateway.cards.client import CardsGatewayGRPCClient, build_cards_gateway_grpc_client
from clients.grpc.gateway.accounts.client import AccountsGatewayGRPCClient, build_accounts_gateway_grpc_client
from clients.grpc.gateway.operations.client import OperationsGatewayGRPCClient, build_operations_gateway_grpc_client

from clients.http.gateway.users.client import UsersGatewayHTTPClient, build_users_gateway_http_client
from clients.http.gateway.cards.client import CardsGatewayHTTPClient, build_cards_gateway_http_client
from clients.http.gateway.accounts.client import AccountsGatewayHTTPClient, build_accounts_gateway_http_client
from clients.http.gateway.operations.client import OperationsGatewayHTTPClient, build_operations_gateway_http_client

from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedAccountsPlan
from seeds.schema.result import SeedsResult, SeedUserResult, SeedAccountResult, SeedCardResult, SeedOperationResult


class SeedsBuilder:
    """
    SeedsBuilder - генератор (сидер), формирующий необходимые тестовые или демонстрационные данные
    на основании входного плана. Работает для gRPC и HTTP клиентов

    users_gateway_client: Клиент для работы с пользователями
    cards_gateway_client: Клиент для работы с картами
    accounts_gateway_client: клиент для работы со счетами
    operations_gateway_client: клиент для работы с операциями
    """

    def __init__(
            self,
            users_gateway_client: UsersGatewayGRPCClient | UsersGatewayHTTPClient,
            cards_gateway_client: CardsGatewayGRPCClient | CardsGatewayHTTPClient,
            accounts_gateway_client: AccountsGatewayGRPCClient | AccountsGatewayHTTPClient,
            operations_gateway_client: OperationsGatewayGRPCClient | OperationsGatewayHTTPClient
    ):
        self.users_gateway_client = users_gateway_client
        self.cards_gateway_client = cards_gateway_client
        self.accounts_gateway_client = accounts_gateway_client
        self.operations_gateway_client = operations_gateway_client

    def build_savings_accounts_result(self, user_id: str) -> SeedAccountResult:
        """
       Открывает сберегательный счет для пользователя.

       :param user_id: Идентификатор пользователя
       :return:
           SeedAccountResult: Результат с идентификатором созданного счета
       """
        response = self.accounts_gateway_client.open_savings_account(user_id=user_id)
        return SeedAccountResult(account_id=response.account.id)

    def build_deposit_accounts_result(self, user_id: str) -> SeedAccountResult:
        """
        Открывает депозитный счет для пользователя.

        :param user_id: Идентификатор пользователя
        :return:
            SeedAccountResult: Результат с идентификатором созданного счета
        """
        response = self.accounts_gateway_client.open_deposit_account(user_id=user_id)
        return SeedAccountResult(account_id=response.account.id)

    def build_physical_card_result(self, user_id: str, account_id: str) -> SeedCardResult:
        """
        Выполняет выпуск физической карты

        :param user_id: Идентификатор пользователя
        :param account_id: Идентификатор счета
        :return:
            SeedCardResult: Результат с идентификатором карты
        """
        response = self.cards_gateway_client.issue_physical_card(
            user_id=user_id,
            account_id=account_id
        )
        return SeedCardResult(card_id=response.card.id)

    def build_transfer_operation_result(self, card_id: str, account_id: str) -> SeedOperationResult:
        """
        Выполняет операцию перевода.

        :param card_id: Идентификатор карты
        :param account_id: Идентификатор аккаунта
        :return:
            SeedOperationResult: Результат с идентификатором операции
        """

        response = self.operations_gateway_client.make_transfer_operation(
            card_id=card_id,
            account_id=account_id
        )
        return SeedOperationResult(operation_id=response.operation.id)

    def build_cash_withdrawal_operation_result(self, card_id: str, account_id: str) -> SeedOperationResult:
        """
        Выполняет операцию снятия средств.

        :param card_id: Идентификатор карты
        :param account_id: Идентификатор аккаунта
        :return:
            SeedOperationResult: Результат с идентификатором операции
        """

        response = self.operations_gateway_client.make_cash_withdrawal_operation(
            card_id=card_id,
            account_id=account_id
        )
        return SeedOperationResult(operation_id=response.operation.id)

    def build_top_up_operation_result(self, card_id: str, account_id: str) -> SeedOperationResult:
        """
        Выполняет операцию пополнения.

        :param card_id: Идентификатор карты
        :param account_id: Идентификатор аккаунта
        :return:
            SeedOperationResult: Результат с идентификатором операции
        """

        response = self.operations_gateway_client.make_top_up_operation(
            card_id=card_id,
            account_id=account_id
        )
        return SeedOperationResult(operation_id=response.operation.id)

    def build_purchase_operation_result(self, card_id: str, account_id: str) -> SeedOperationResult:
        """
        Выполняет операцию оплаты.

        :param card_id: Идентификатор карты
        :param account_id: Идентификатор аккаунта
        :return:
            SeedOperationResult: Результат с идентификатором операции
        """
        response = self.operations_gateway_client.make_purchase_operation(
            card_id=card_id,
            account_id=account_id
        )
        return SeedOperationResult(operation_id=response.operation.id)

    def build_virtual_card_result(self, user_id: str, account_id: str) -> SeedCardResult:
        """
        Выполняет выпуск виртуальной карты

        :param user_id: Идентификатор пользователя
        :param account_id: Идентификатор счета
        :return:
            SeedCardResult: Результат с идентификатором карты
        """
        response = self.cards_gateway_client.issue_physical_card(
            user_id=user_id,
            account_id=account_id
        )
        return SeedCardResult(card_id=response.card.id)

    def build_debit_card_accounts_result(self, user_id: str, plan: SeedAccountsPlan) -> SeedAccountResult:
        """
        Открывает дебетовый счет и выполняет действия согласно плану:
        - выпускает физические карты
        - выполняет операции пополнения
        - выполняет операции покупки

        :param user_id: Идентификатор пользователя
        :param plan: План создания дебетового счета
        :return:
            SeedAccountResult: Результат с идентификаторами счета и деталями операций
        """
        response = self.accounts_gateway_client.open_debit_card_account(user_id=user_id)
        account_id = response.account.id
        card_id = response.account.cards[0].id

        return SeedAccountResult(
            account_id=response.account.id,
            physical_card=[
                self.build_physical_card_result(user_id=user_id, account_id=account_id)
                for _ in range(plan.physical_card.count)
            ],
            top_up_operations=[
                self.build_top_up_operation_result(card_id=card_id, account_id=account_id)
                for _ in range(plan.top_up_operations.count)
            ],
            purchase_operations=[
                self.build_purchase_operation_result(card_id=card_id, account_id=account_id)
                for _ in range(plan.purchase_operations.count)
            ],
            virtual_card=[
                self.build_virtual_card_result(user_id=user_id, account_id=account_id)
                for _ in range(plan.virtual_card.count)
            ],
            transfer_operations=[
                self.build_transfer_operation_result(card_id=card_id, account_id=account_id)
                for _ in range(plan.top_up_operations.count)
            ],
            cash_withdrawal_operations=[
                self.build_cash_withdrawal_operation_result(card_id=card_id, account_id=account_id)
                for _ in range(plan.top_up_operations.count)
            ],
        )

    def build_credit_card_accounts_result(self, user_id: str, plan: SeedAccountsPlan) -> SeedAccountResult:
        """
        Открывает кредитный счет и выполняет действия согласно плану:
        - выпускает физические карты
        - выполняет операции пополнения
        - выполняет операции покупки

        :param user_id: Идентификатор пользователя
        :param plan: План создания кредитного счета
        :return:
            SeedAccountResult: Результат с идентификаторами счета и деталями операций
        """
        response = self.accounts_gateway_client.open_credit_card_account(user_id=user_id)
        account_id = response.account.id
        card_id = response.account.cards[0].id

        return SeedAccountResult(
            account_id=response.account.id,
            physical_card=[
                self.build_physical_card_result(user_id=user_id, account_id=account_id)
                for _ in range(plan.physical_card.count)
            ],
            top_up_operations=[
                self.build_top_up_operation_result(card_id=card_id, account_id=account_id)
                for _ in range(plan.top_up_operations.count)
            ],
            purchase_operations=[
                self.build_purchase_operation_result(card_id=card_id, account_id=account_id)
                for _ in range(plan.purchase_operations.count)
            ],
            virtual_card=[
                self.build_virtual_card_result(user_id=user_id, account_id=account_id)
                for _ in range(plan.virtual_card.count)
            ],
            transfer_operations=[
                self.build_transfer_operation_result(card_id=card_id, account_id=account_id)
                for _ in range(plan.top_up_operations.count)
            ],
            cash_withdrawal_operations=[
                self.build_cash_withdrawal_operation_result(card_id=card_id, account_id=account_id)
                for _ in range(plan.top_up_operations.count)
            ],
        )

    def build_user(self, plan: SeedUsersPlan) -> SeedUserResult:
        """
        Создает пользователя согласно созданному плану:
        - открывает сберегательные и депозитные счета
        - создает дебетовые и кредитные счета с картами и операциями

        :param
            plan: План генерации пользователя

        :return:
            SeedUserResult: Результат с идентификатором пользователя и всеми созданными сущностями.
        """
        response = self.users_gateway_client.create_user()

        return SeedUserResult(
            user_id=response.user.id,
            deposit_accounts=[
                self.build_deposit_accounts_result(user_id=response.user.id)
                for _ in range(plan.deposit_accounts.count)
            ],
            savings_accounts=[
                self.build_savings_accounts_result(user_id=response.user.id)
                for _ in range(plan.savings_accounts.count)
            ],
            debit_card_accounts=[
                self.build_debit_card_accounts_result(user_id=response.user.id, plan=plan.debit_card_accounts)
                for _ in range(plan.debit_card_accounts.count)
            ],
            credit_card_accounts=[
                self.build_credit_card_accounts_result(user_id=response.user.id, plan=plan.credit_card_accounts)
                for _ in range(plan.credit_card_accounts.count)
            ]
        )

    def build(self, plan: SeedsPlan) -> SeedsResult:
        """
        Генерирует полную структуру данных на основе плана:
        - создает указанное количество пользователей
        - каждому пользователю присваиваются счета, пользователи, операции
        :Args:
            plan: Полный план генерации данных
        :return:
            SeedsResult: Результат с данными всех созданных пользователей
        """
        return SeedsResult(users=[self.build_user(plan.users) for _ in range(plan.users.count)])


def build_grpc_seeds_builder() -> SeedsBuilder:
    """
    Фабрика для создания сидера с использованием gRPC-клиентов.

    :return:
        SeedsBuilder: Инициализированный сидер с использованием gRPC-клиентов.
    """
    return SeedsBuilder(
        users_gateway_client=build_users_gateway_grpc_client(),
        cards_gateway_client=build_cards_gateway_grpc_client(),
        accounts_gateway_client=build_accounts_gateway_grpc_client(),
        operations_gateway_client=build_operations_gateway_grpc_client()
    )


def build_http_seeds_builder() -> SeedsBuilder:
    """
    Фабрика для создания сидера с использованием HTTP-клиентов.

    :return:
        SeedsBuilder: Инициализированный сидер с использованием HTTP-клиентов.
    """
    return SeedsBuilder(
        users_gateway_client=build_users_gateway_http_client(),
        cards_gateway_client=build_cards_gateway_http_client(),
        accounts_gateway_client=build_accounts_gateway_http_client(),
        operations_gateway_client=build_operations_gateway_http_client()
    )
