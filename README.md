# GoCardless API Demonstration

This repository provides a basic demonstration of how to connect to the **GoCardless API** and retrieve data related to bank accounts, requisitions, and more. It is designed to show how you can programmatically interact with GoCardless' services. Later, it can be extended to suit your needs for processing or storing the data.

---

### **Prerequisites**

1. **Create an Account**:
   - Visit [GoCardless Bank Account Data](https://bankaccountdata.gocardless.com).
   - Sign up for an account and generate your credentials (secret ID and secret key).
   
2. **Install Dependencies**:
   
   To install the required dependencies, run the following:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Credentials**:
   - After registering, download or manually copy the `credentials.json` file into the `credentials/` folder.
   - Ensure that the file contains your **secret ID** and **secret key**.

---

### **How to Use**

1. **Running the Scripts**:
   The scripts in this repository allow you to interact with the GoCardless API. Here is how you can use each one:

   - **`api-token.py`**: Generates an API token that you can use to authenticate API requests. It can be used for testing purposes at [swagger](https://developer.gocardless.com/bank-account-data/endpoints/).
     ```bash
     python api-token.py
     ```

   - **`add-requisition.py`**: Adds an account by creating a requisition. You will need to follow a link for verification and approval.
     ```bash
     python add-requisition.py
     ```

   - **`show-requisitions.py`**: Retrieves and displays all requisitions, including account details if available.
     ```bash
     python show-requisitions.py
     ```

   - **`delete-requisition.py`**: Deletes a specific requisition. The script will prompt you to enter a requisition ID.
     ```bash
     python delete-requisition.py
     ```

   - **`account-info.py`**: Fetches and displays details of a specific account using the account ID.
     ```bash
     python account-info.py
     ```

---

### **File Descriptions**

- **`account-info.py`**: Retrieves details for a given account (IBAN, Owner, Currency). You will need to provide an account ID.
- **`add-requisition.py`**: Starts the process of adding an account by creating a requisition. You will receive a verification URL that you must follow to complete the process.
- **`api-token.py`**: This script generates an authentication token that you need to use in the other scripts.
- **`delete-requisition.py`**: Prompts for a requisition ID and deletes the corresponding requisition. This is useful when you need to clean up test requisitions.
- **`show-requisitions.py`**: Lists all requisitions created in your GoCardless account, including the associated accounts (e.g., EUR, USD).
- **`credentials/credentials.json`**: Store your GoCardless API credentials here (secret ID and secret key).
- **`requirements.txt`**: Lists the Python dependencies required to run the scripts.

---

### **Important Notes**

- **Rate Limiting**: Be aware that fetching account details is rate-limited to **4 times per day**. Be sure to plan accordingly to avoid hitting the limit.
  
- **GoCardless Setup**:
  - When adding a new account, you will need to create a requisition (e.g., for Revolut Bank). This will generate a URL for account verification. Follow the steps to complete the process.
  - Once verification is complete, you can retrieve the requisition details, including the accounts (e.g., EUR, USD, etc.) linked to it.
  
---

### **Credits**

This project was inspired by [GoCardless to CSV](https://github.com/adept/gocardless-to-csv). It provides a basic framework for interacting with the GoCardless API, which can be expanded for further integrations.
