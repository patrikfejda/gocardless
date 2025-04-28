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

def main():
    secret_id, secret_key = load_secrets()
    token = get_api_token(secret_id, secret_key)
    print(token)

if __name__ == "__main__":
    main()
