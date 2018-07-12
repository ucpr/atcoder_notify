import json
import requests

URL = "http://kenkoooo.com/atcoder/atcoder-api/info/ac"
with open("users.json", "r") as f:
    users = json.load(f)["users"]["atcoder"]


def save(data):
    with open("ac_count.json", "w") as f:
        json.dump(data, f)
        print("save -> ac_count.json")


def main():
    result = dict()
    r = requests.get(URL)
    ac_data = json.loads(r.text)
    for i in filter(lambda x: x["user_id"] in users, ac_data):
        result[i["user_id"]] = i["problem_count"]

    save(result)  # save ac_count


if __name__ == "__main__":
    main()
