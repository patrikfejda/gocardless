import json
import requests

CREDENTIALS_PATH = 'credentials/credentials.json'
BASE_URL = "https://bankaccountdata.gocardless.com/api/v2"

def load_secrets(path=CREDENTIALS_PATH):
    with open(path) as file:
        creds = json.load(file)
    return creds['secret_id'], creds['secret_key']

def make_request(method, endpoint, token=None, json_body=None):
    url = f"{BASE_URL}{endpoint}"
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    if token:
        headers['Authorization'] = f'Bearer {token}'
    response = requests.request(method, url, headers=headers, json=json_body)
    response.raise_for_status()
    return response.json()

def get_api_token(secret_id, secret_key):
    payload = {'secret_id': secret_id, 'secret_key': secret_key}
    return make_request('POST', '/token/new/', json_body=payload).get('access')

def delete_requisition(token, requisition_id):
    url = f"/requisitions/{requisition_id}/"
    try:
        response = make_request('DELETE', url, token=token)
        print(f"Requisition {requisition_id} deleted successfully." if response else f"Failed to delete requisition {requisition_id}.")
    except Exception as e:
        print(f"Error deleting requisition {requisition_id}: {e}")

def main():
    secret_id, secret_key = load_secrets()
    token = get_api_token(secret_id, secret_key)
    
    requisition_id = input("Enter the requisition ID to delete: ")
    delete_requisition(token, requisition_id)

if __name__ == "__main__":
    main()
