import requests
import json

URL = "https://api.github.com/users/mitohato/events"
r = requests.get(URL)
print(r.text)
