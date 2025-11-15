from locust import User, task, between

from clients.grpc.gateway.users.client import UsersGatewayGRPCClient, build_users_gateway_locust_grpc_client
from clients.grpc.gateway.accounts.client import AccountsGatewayGRPCClient, build_accounts_gateway_locust_grpc_client
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse


class GetUserScenarioUser(User):
    host = "localhost"
    wait_time = between(1, 3)
    user_gateway_client: UsersGatewayGRPCClient
    account_gateway_client: AccountsGatewayGRPCClient
    create_user_response: CreateUserResponse

    def on_start(self) -> None:
        self.user_gateway_client = build_users_gateway_locust_grpc_client(self.environment)
        self.account_gateway_client = build_accounts_gateway_locust_grpc_client(self.environment)
        self.create_user_response = self.user_gateway_client.create_user()

    @task
    def open_debit_card_account(self):
        self.account_gateway_client.open_debit_card_account(self.create_user_response.user.id)
