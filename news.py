import requests
SEND_KEY = "SCT340534Tkb8yYcTXtIjOkOBKHNK7EQTw"

def get_news():
    url = "https://www.cls.cn/api/sw?app=CailianpressWeb&os=web&sv=7.7.5&action=getRollingNews&lastTime=0&lastId=0&pageSize=5&channel=finance"
    response = requests.get(url)
    data = response.json().get('data', [])
    news = ["【今日金融早报】"]
    for i, item in enumerate(data):
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
