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

get_document_tariff_response = httpx.get(f"http://localhost:8003/api/v1/documents/tariff-document/{account_id}")

get_document_tariff_response_data = get_document_tariff_response.json()

print("Get tariff document response: ", get_document_tariff_response_data)
print("Get tariff document status code: ", get_document_tariff_response.status_code)

get_document_contract_response = httpx.get(f"http://localhost:8003/api/v1/documents/contract-document/{account_id}")

get_document_contract_response_data = get_document_contract_response.json()

print("Get contract document response: ", get_document_contract_response_data)
print("Get contract document status code: ", get_document_contract_response.status_code)
