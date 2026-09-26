import requests
import datetime
import json
import os

today = datetime.date.today().isoformat()
url = f"https://events.umich.edu/list/json?range={today}&v=2"

resp = requests.get(url, timeout=15)
resp.raise_for_status()

os.makedirs("docs", exist_ok=True)
with open("docs/events.json", "w") as f:
    json.dump(resp.json(), f)

print(f"Fetched {len(resp.json())} events for {today}")
