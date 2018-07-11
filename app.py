import requests
import xml.etree.ElementTree as ET

URL = "https://github.com/users/nve3pd/contributions"
response = requests.get(URL)
root = ET.fromstring(response.text)

commits = 0
for e in root.getiterator("rect"):
    if e.get("data-date") in "2018-07-10":
        commits = e.get("data-count")

print (commits)
