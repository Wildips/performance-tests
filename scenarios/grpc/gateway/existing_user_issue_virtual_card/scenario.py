from locust import task, events
from locust.env import Environment

from clients.grpc.gateway.locust import GatewayGRPCTaskSet
from contracts.services.accounts.rpc_get_account_pb2 import GetAccountResponse
from seeds.scenarios.existing_user_issue_virtual_card import ExistingUserIssueVirtualCardSeedsScenario
from seeds.schema.result import SeedUserResult
from tools.locust.user import LocustBaseUser


@events.init.add_listener
def init(environment: Environment, **kwargs):
    seeds_scenario = ExistingUserIssueVirtualCardSeedsScenario()
    seeds_scenario.build()

    environment.seeds = seeds_scenario.load()


class IssueVirtualCardTaskSet(GatewayGRPCTaskSet):
    get_accounts_response: GetAccountResponse | None = None
    seed_user: SeedUserResult

    def on_start(self) -> None:
        super().on_start()
        self.seed_user = self.user.environment.seeds.get_random_user()

    @task(2)
    def get_accounts(self):
        self.get_accounts_response = self.accounts_gateway_client.get_accounts(
            user_id=self.seed_user.user_id
        )

    @task(1)
    def make_virtual_card(self):
        if not self.get_accounts_response:
            return

        self.cards_gateway_client.issue_virtual_card(
            user_id=self.seed_user.user_id,
            account_id=self.get_accounts_response.accounts[0].id
        )


class MakeVirtualCardsUser(LocustBaseUser):
    tasks = [IssueVirtualCardTaskSet]
