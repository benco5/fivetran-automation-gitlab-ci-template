import os
import json
import requests

BASE64_API_KEY = os.environ.get("FIVETRAN_BASE64_API_KEY")
CONNECTION_ID = os.environ.get("CONNECTION_ID")
BASE_URL = f"https://api.fivetran.com/v1/connections/{CONNECTION_ID}/sync"
SYNC_PAYLOAD = {"force": True}

headers = {
    "Accept": "application/json;version=2",
    "Authorization": f"Basic {BASE64_API_KEY}",
    "content-type": "application/json"
}

def force_sync():
    try:
        response = requests.request("POST", BASE_URL, json=SYNC_PAYLOAD, headers=headers)

        response.raise_for_status()

        parsed_body = response.json()
        formatted_body = json.dumps(parsed_body, indent=4)
        print(formatted_body)
    except json.JSONDecodeError as e:
        print(f"An error occurred while decoding JSON: {e}")
    except requests.exceptions.RequestException as e:
        print(f"There was an issue when trying to force syncing of the connection {CONNECTION_ID}: {e}.")

if __name__ == "__main__":
    force_sync()