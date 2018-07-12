import json
import requests

URL = "http://kenkoooo.com/atcoder/atcoder-api/info/ac"
with open("users.json", "r") as f:
    users = json.load(f)["users"]["atcoder"]


def save(data):
    """ 結果をac_count.jsonに結果を保存させる """
    with open("ac_count.json", "w") as f:
        json.dump(data, f)
        print("save -> ac_count.json")


def get_no1(data):
    """ 前回から最もACした人を返す """
    res = [None, 0]
    with open("ac_count.json", "r") as f:
        last_time = json.load(f)  # 前回の結果をload
    for i in data.items():  # i -> ("name", count)
        if i[1] - last_time[i[0]] > res[1]:
            res[0] = i[0]  # name
            res[1] = i[1] - last_time[i[0]]  # AC count
    return res


def getAC():
    result = dict()
    r = requests.get(URL)
    ac_data = json.loads(r.text)
    for i in filter(lambda x: x["user_id"] in users, ac_data):
        result[i["user_id"]] = i["problem_count"]

    save(result)  # save ac_count
    return get_no1(result)


if __name__ == "__main__":
    print(getAC())
