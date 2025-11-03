from locust import User, task, between

from clients.http.gateway.users.client import UsersGatewayHTTPClient, build_users_gateway_locust_http_client
from clients.http.gateway.users.schema import CreateUserResponseSchema


class GetUserScenarioUser(User):
    http = "localhost"
    wait_time = between(1, 3)
    user_gateway_client: UsersGatewayHTTPClient
    create_user_response: CreateUserResponseSchema

    def on_start(self) -> None:
        self.user_gateway_client = build_users_gateway_locust_http_client(self.environment)
        self.create_user_response = self.user_gateway_client.create_user()

    @task
    def get_user(self):
        self.user_gateway_client.get_user(self.create_user_response.user.id)
