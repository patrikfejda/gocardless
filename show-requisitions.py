import json
import requests

CREDENTIALS_PATH = 'credentials/credentials.json'
BASE_URL = "https://bankaccountdata.gocardless.com/api/v2"

def load_secrets(path=CREDENTIALS_PATH):
    with open(path) as file:
        creds = json.load(file)
    return creds['secret_id'], creds['secret_key']

def get_api_token(secret_id, secret_key):
    url = f"{BASE_URL}/token/new/"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    payload = {'secret_id': secret_id, 'secret_key': secret_key}
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json().get('access')

def get_all_requisitions(token):
    url = f"{BASE_URL}/requisitions/"
    headers = {'Authorization': f'Bearer {token}', 'Accept': 'application/json'}
    response = requests.get(url, headers=headers)
    if not response.ok:
        print(f"Failed to retrieve requisitions. Status: {response.status_code}\n{response.text}")
        return []

    print("Requisitions retrieved successfully.")
    for req in response.json().get('results', []):
        print(f"\n{'-'*50}\nRequisition: {req['id']}\nReference: {req['reference']}\nAccounts: {req['accounts']}\n{'-'*50}")
    return response.json().get('results', [])

def main():
    secret_id, secret_key = load_secrets()
    token = get_api_token(secret_id, secret_key)
    get_all_requisitions(token)

if __name__ == "__main__":
    main()
