import httpx
import time

create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string",
}

create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
user_id = create_user_response_data['user']['id']

open_credit_card_account_payload = {
    "userId": user_id
}
open_credit_card_account_response = httpx.post("http://localhost:8003/api/v1/accounts/open-credit-card-account",
                                               json=open_credit_card_account_payload)

open_credit_card_account_response_data = open_credit_card_account_response.json()
account_id = open_credit_card_account_response_data['account']['id']
first_card_id = open_credit_card_account_response_data['account']['cards'][0]['id']

make_purchase_operation_payload = {
    "status": "IN_PROGRESS",
    "amount": 77.99,
    "category": "taxi",
    "cardId": first_card_id,
    "accountId": account_id,
}
make_purchase_operation_response = httpx.post("http://localhost:8003/api/v1/operations/make-purchase-operation",
                                              json=make_purchase_operation_payload)
make_purchase_operation_response_data = make_purchase_operation_response.json()

operation_id = make_purchase_operation_response_data['operation']['id']
print("Make purchase operation response: ", make_purchase_operation_response_data)
print("Make purchase operation status code: ", make_purchase_operation_response.status_code)
print("Make purchase operation ID: ", operation_id)
