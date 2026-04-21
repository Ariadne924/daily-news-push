import requests
SEND_KEY = "SCT340534Tkb8yYcTXtIjOkOBKHNK7EQTw"

def get_news():
    url = "https://api.toutiao.com/api/pc/feed/?category=finance&utm_source=toutiao&widen=1&max_behot_time=0"
    response = requests.get(url)
    data = response.json().get("data", [])
    news = ["【今日金融早报】"]
    for i, item in enumerate(data[:5]):
        news.append(f"{i+1}. {item.get('title', '无标题')}")
    return "\n".join(news)

def push_news():
    content = get_news()
    requests.post(
        f"https://sctapi.ftqq.com/{SEND_KEY}.send",
        data={"text": "今日金融早报", "desp": content}
    )

if __name__ == "__main__":
    push_news()
