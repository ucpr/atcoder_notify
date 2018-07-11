import requests
import xml.etree.ElementTree as ET
from datetime import date, timedelta

URL = "https://github.com/users/nve3pd/contributions"
response = requests.get(URL)
root = ET.fromstring(response.text)

yesterday = date.today() - timedelta(days = 1)
print (yesterday)

commits = 0
for e in root.getiterator("rect"):
    if e.get("data-date") in yesterday.isoformat():
        commits = e.get("data-count")

print (commits)
