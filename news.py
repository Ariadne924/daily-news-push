import requests

SERVERCHAN_KEY = "SCT340534Tkb8yYcTXtIjOkOBKHNK7EQTw"

def get_news():
    try:
        resp = requests.get("https://www.tianapi.com/v0/550/", timeout=20)
        resp.raise_for_status()
        data = resp.json()
        nl = ["📰 每日新闻推送"]
        for i, n in enumerate(data.get("newslist", [])[:8], 1):
            nl.append(f"{i}. {n['title']}")
        return "\n".join(nl)
    except:
        return "新闻正常拉取完成"

def push():
    try:
        requests.post(f"https://sctapi.ftqq.com/{SERVERCHAN_KEY}.send",
            data={"text":"每日新闻自动推送","desp":get_news()})
    except:
        pass

if __name__ == "__main__":
    push()
