import requests
import os

# Set these values
ACTIONS_TOKEN = os.getenv("ACTIONS_TOKEN")
OWNER = "ogyct"
REPO = "BIM-POC"

headers = {
    "Authorization": f"Bearer {ACTIONS_TOKEN}",
    "Accept": "application/vnd.github+json"
}

url = f"https://api.github.com/repos/{OWNER}/{REPO}/actions/workflows"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    workflows = response.json().get("workflows", [])
    print(f"Found {len(workflows)} workflows:")
    for wf in workflows:
        print(f"- {wf['name']} (id: {wf['id']})")
else:
    print(f"Failed to fetch workflows: {response.status_code}")
    print(response.text)