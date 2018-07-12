import requests
import xml.etree.ElementTree as ET
from datetime import date, timedelta
import json

proxies = {
    'http': 'http://cproxy.okinawa-ct.ac.jp:8080',
    'https': 'http://cproxy.okinawa-ct.ac.jp:8080',
}

def get_xml(getURL):
    response = requests.get(getURL, proxies=proxies)
    root = ET.fromstring(response.text)
    return root

def get_date():
    yesterday = date.today() - timedelta(days = 1)
    print (yesterday)
    return yesterday.isoformat()

def get_commits_number(root, yesterday):
    commits = 0
    for e in root.getiterator('rect'):
        if e.get('data-date') in yesterday:
            commits = e.get('data-count')

    print (commits)
    return commits

def json_read():
    with open('users.json', 'r') as f:
        data = json.load(f)
        print(data)
    return data

if __name__ == '__main__':
    j_data = json_read()
    users = j_data["users"]["github"]
    URL = 'https://github.com/users/'

    root = get_xml(URL)
    date = get_date()
    commits = get_commits_number(root, date)

    print (commits)
