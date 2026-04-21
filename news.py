import requests

KEY = "SCT340534Tkb8yYcTXtIjOkOBKHNK7EQTw"

def get():
    try:
        r = requests.get("https://www.reddit.com/r/worldnews/hot.json?limit=8", timeout=15)
        j = r.json()
        arr = ["🌍 全球新闻早报"]
        for c in j["data"]["children"]:
            arr.append(f"- {c['data']['title']}")
        return "\n".join(arr)
    except:
        return "拉取完成"

requests.post(f"https://sctapi.ftqq.com/{KEY}.send",
data={"text":"每日新闻推送","desp":get()})
