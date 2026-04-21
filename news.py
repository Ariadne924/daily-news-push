import requests
from bs4 import BeautifulSoup
SEND_KEY = "SCT340534Tkb8yYcTXtIjOkOBKHNK7EQTw"

def get_news():
    url = "https://finance.sina.com.cn/roll/index.d.html?cid=56588"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")
    news_list = soup.select(".list_009 li a")[:5]
    news = ["【今日金融早报】"]
    for i, item in enumerate(news_list):
        news.append(f"{i+1}. {item.get_text(strip=True)}")
    return "\n".join(news) if len(news) > 1 else "今日暂无新闻"

def push_news():
    content = get_news()
    requests.post(
        f"https://sctapi.ftqq.com/{SEND_KEY}.send",
        data={"text": "今日金融早报", "desp": content}
    )

if __name__ == "__main__":
    push_news()
