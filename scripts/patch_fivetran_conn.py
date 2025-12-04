import os
import json
import requests

BASE64_API_KEY = os.environ.get("FIVETRAN_BASE64_API_KEY")
CONNECTION_ID = os.environ.get("CONNECTION_ID")
PATCH_PAYLOAD = os.environ.get("PATCH_PAYLOAD")
BASE_URL = f"https://api.fivetran.com/v1/connections/{CONNECTION_ID}"

headers = {
    "Accept": "application/json;version=2",
    "Authorization": f"Basic {BASE64_API_KEY}",
    "content-type": "application/json"
}

def patch_update():

    if not PATCH_PAYLOAD:
        raise ValueError("PATCH_PAYLOAD is required but was not found.")

    try:
        patch_body = json.loads(PATCH_PAYLOAD)
        response = requests.request("PATCH", BASE_URL, json=patch_body, headers=headers)

        response.raise_for_status()

        resp_json = response.json()
        formatted_json = json.dumps(resp_json, indent=4)
        print(formatted_json)
    except json.JSONDecodeError as e:
        print(f"Unable to parse the PATCH_PAYLOAD value: {e}")
    except requests.exceptions.RequestException as e:
        print(f"There was an issue when trying to update the connection {CONNECTION_ID}: {e}.")

if __name__ == "__main__":
    patch_update()
