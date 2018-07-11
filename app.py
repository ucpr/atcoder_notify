import json
import requests

with open("env.json", "r") as f:
    URL = json.load(f)["webhook_URL"]


def main():
    p = {"text": "Hello World!"}
    headers = {"content-type": "application/json"}
    r = requests.post(URL, data=json.dumps(p), headers=headers)
    print(r.text)


if __name__ == "__main__":
    main()
