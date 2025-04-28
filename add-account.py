import json
from nordigen import NordigenClient

CREDENTIALS_PATH = "credentials/credentials.json"
REDIRECT_URI = "https://webhook.site/01b32a2f-9389-4167-9397-4e198d9fff9b"

def load_credentials(path=CREDENTIALS_PATH):
    with open(path) as f:
        creds = json.load(f)
    return creds["secret_id"], creds["secret_key"]

def select_institution(client, country_code):
    institutions = client.institution.get_institutions(country_code)
    print("Available institutions:")
    for inst in institutions:
        print(f"{inst['name']} (ID: {inst['id']})")
    name = input("Enter the institution name: ")
    return next((inst for inst in institutions if inst['name'] == name), None)

def add_account(client):
    country_code = input("Enter the country code (e.g., 'SK'): ")
    institution = select_institution(client, country_code)
    if not institution:
        print("Institution not found.")
        return

    reference_id = f"{input('Your name and surname: ')} {institution['name']}"
    init = client.initialize_session(
        institution_id=institution['id'],
        redirect_uri=REDIRECT_URI,
        reference_id=reference_id,
        max_historical_days=institution['transaction_total_days'],
        access_valid_for_days=institution['max_access_valid_for_days']
    )
    print(f"Go to this link to finish authorization:\n{init.link}")

def main():
    secret_id, secret_key = load_credentials()
    client = NordigenClient(secret_id=secret_id, secret_key=secret_key)
    client.generate_token()
    add_account(client)

if __name__ == "__main__":
    main()
