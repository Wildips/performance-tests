from locust import task, events
from locust.env import Environment

from clients.grpc.gateway.locust import GatewayGRPCTaskSet
from contracts.services.accounts.rpc_get_account_pb2 import GetAccountResponse
from contracts.services.gateway.operations.rpc_get_operations_pb2 import GetOperationsResponse
from seeds.schema.result import SeedUserResult
from tools.locust.user import LocustBaseUser
from seeds.scenarios.existing_user_get_operations import ExistingUserGetOperationsSeedsScenario


@events.init.add_listener
def init(environment: Environment, **kwargs):
    seeds_scenario = ExistingUserGetOperationsSeedsScenario()
    seeds_scenario.build()

    environment.seeds = seeds_scenario.load()


class GetOperationsTaskSet(GatewayGRPCTaskSet):
    get_accounts_response: GetAccountResponse | None = None
    seed_user: SeedUserResult
    get_operations_response: GetOperationsResponse

    def on_start(self) -> None:
        super().on_start()
        self.seed_user = self.user.environment.seeds.get_random_user()

    @task(1)
    def create_accounts(self):
        self.get_accounts_response = self.accounts_gateway_client.get_accounts(
            user_id=self.seed_user.user_id
        )

    @task(3)
    def get_operations(self):
        if not self.get_accounts_response:
            return

        self.get_operations_response = self.operations_gateway_client.get_operations(
            account_id=self.get_accounts_response.accounts[0].id
        )

    @task(3)
    def get_operation_summary(self):
        if not self.get_accounts_response:
            return

        self.operations_gateway_client.get_operations_summary(
            account_id=self.get_accounts_response.accounts[0].id
        )


class GetOperationsUser(LocustBaseUser):
    tasks = [GetOperationsTaskSet]
