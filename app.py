import requests
import xml.etree.ElementTree as ET

URL = "https://github.com/users/mitohato/contributions"
response = requests.get(URL)
root = ET.fromstring(response.text)
print(root.tag)
