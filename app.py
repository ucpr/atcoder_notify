import json
import requests

TEMPLATE = """
{0}半端ないって！
あいつ半端ないって！
{0}めっちゃ{1}もん
そんなの出来ひんやん 普通
そんなんできる？
言っといてや出来るんやったら
"""
with open("env.json", "r") as f:
    URL = json.load(f)["webhook_URL"]


def mktext(f, name):
    result = TEMPLATE.format(name, "ACする" if f == "atcoder" else "草生やす")
    return result


def main():
    p = {"text": mktext}
    headers = {"content-type": "application/json"}
    r = requests.post(URL, data=json.dumps(p), headers=headers)
    print(r.text)


if __name__ == "__main__":
    main()
