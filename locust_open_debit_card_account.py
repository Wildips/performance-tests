from locust import User, task, between

from clients.http.gateway.users.client import UsersGatewayHTTPClient, build_users_gateway_locust_http_client
from clients.http.gateway.users.schema import CreateUserResponseSchema
from clients.http.gateway.accounts.client import AccountsGatewayHTTPClient, build_accounts_gateway_locust_http_client


class GetUserScenarioUser(User):
    host = "localhost"
    wait_time = between(1, 3)
    user_gateway_client: UsersGatewayHTTPClient
    account_gateway_client: AccountsGatewayHTTPClient
    create_user_response: CreateUserResponseSchema

    def on_start(self) -> None:
        self.user_gateway_client = build_users_gateway_locust_http_client(self.environment)
        self.account_gateway_client = build_accounts_gateway_locust_http_client(self.environment)
        self.create_user_response = self.user_gateway_client.create_user()

    @task
    def open_debit_card_account(self):
        self.account_gateway_client.open_debit_card_account(self.create_user_response.user.id)
