import requests

SERVERCHAN_KEY = "SCT340534Tkb8yYcTXtIjOkOBKHNK7EQTw"

def get_news():
    urls = [
        "https://newsapi.ayoung.top/api",
        "https://api.pearktrue.cn/api/60s"
    ]
    for url in urls:
        try:
            r = requests.get(url, timeout=10)
            j = r.json()
            if j.get("code") == 200 or j.get("success"):
                news = ["📈 今日财经早报"]
                for n in j["data"]["news"][:8]:
                    news.append(f"- {n}")
                return "\n".join(news)
        except:
            continue
    return "接口临时波动"

if __name__ == "__main__":
    c = get_news()
    requests.post(f"https://sctapi.ftqq.com/{SERVERCHAN_KEY}.send",
        data={"text":"每日新闻推送","desp":c})
