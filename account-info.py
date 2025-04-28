import json
import requests

CREDENTIALS_PATH = 'credentials/credentials.json'
BASE_URL = "https://bankaccountdata.gocardless.com/api/v2"

def load_secrets(path=CREDENTIALS_PATH):
    with open(path) as file:
        creds = json.load(file)
    return creds['secret_id'], creds['secret_key']

def make_request(method, endpoint, token=None, params=None, json_body=None):
    url = f"{BASE_URL}{endpoint}"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    if token:
        headers['Authorization'] = f'Bearer {token}'
    response = requests.request(method, url, headers=headers, params=params, json=json_body)
    response.raise_for_status()
    return response.json()

def get_api_token(secret_id, secret_key):
    payload = {'secret_id': secret_id, 'secret_key': secret_key}
    return make_request('POST', '/token/new/', json_body=payload).get('access')

def get_account_details(token, account_id):
    try:
        account = make_request('GET', f'/accounts/{account_id}/details/', token=token).get('account', {})
        print("Account details retrieved successfully.")
        print(f"IBAN: {account.get('iban')}")
        print(f"Account Owner: {account.get('ownerName')}")
        print(f"Currency: {account.get('currency')}")
        return account
    except Exception as e:
        print(f"Error fetching account details: {e}")

def get_account_balances(token, account_id):
    try:
        balances = make_request('GET', f'/accounts/{account_id}/balances/', token=token).get('balances', [])
        print("Account balances retrieved successfully.")
        for balance in balances:
            print(balance)
            print("-" * 50)
        return balances
    except Exception as e:
        print(f"Error fetching balances: {e}")

def get_account_transactions(token, account_id):
    try:
        params = {}        
        # params = {'date_from': '2025-01-01', 'date_to': '2025-12-01'}
        transactions = make_request('GET', f'/accounts/{account_id}/transactions/', token=token, params=params).get('transactions', {})
        print("Transactions retrieved successfully.")
        print(transactions)
        return transactions
    except Exception as e:
        print(f"Error fetching transactions: {e}")

def main():
    secret_id, secret_key = load_secrets()
    token = get_api_token(secret_id, secret_key)
    account_id = input("Enter the account ID: ")
    get_account_details(token, account_id)
    get_account_balances(token, account_id)
    get_account_transactions(token, account_id)

if __name__ == "__main__":
    main()
