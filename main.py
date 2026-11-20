import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

api_key = os.getenv("API_KEY")

if not api_key:
    raise RuntimeError("API_KEY MISSING")

url = "https://mcp.dunkapi.com/v1/get_team_stats"

headers = {
    "Content-Type": "application/json",
    "x-api-key": api_key,
}

json={
    "season": "2026",
    "season_type": "regular",
    "team": "UTAH"
}

response = requests.post(
    url, 
    headers=headers,
    json=json
)

print("Status:", response.status_code)
print("Response:", response.text)

response.raise_for_status()

try:
    pprint(response.json())
except ValueError:
    print("JSON not received")