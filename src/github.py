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
    return yesterday.isoformat()


def get_commits_number(root, yesterday):
    commits = 0
    for e in root.getiterator('rect'):
        if e.get('data-date') in yesterday:
            commits = e.get('data-count')

    return commits


def json_read():
    with open('users.json', 'r') as f:
        data = json.load(f)

    return data


def get_commit():
    j_data = json_read()
    users = j_data["users"]["github"]

    date = get_date()
    commits = {}
    sorted_value = []

    for name in users:
        URL = 'https://github.com/users/' + name + '/contributions'
        root = get_xml(URL)
        commits[name] = get_commits_number(root, date)

    sorted_value = sorted(commits.items(), key=lambda x: x[1])

    print (sorted_value[-1])
    return (sorted_value[-1])


if __name__ == "__main__":
    get_commit()
