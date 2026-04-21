import requests
# 把下面引号里的内容换成你自己的Server酱密钥
SEND_KEY = "SCT340534Tkb8yYcTXtIjOkOBKHNK7EQTw"

def get_financial_news():
    # 用新浪财经的公开接口，稳定不拦截
    api_url = "https://v.juhe.cn/toutiao/index?type=caijing&key=你可以去聚合数据申请一个免费的key"
    # 如果不想申请key，也可以用这个备用的静态新闻接口：
    # api_url = "https://api.oioweb.cn/api/news/toutiao?type=caijing"
    
    response = requests.get(api_url, timeout=5)
    news_data = response.json().get("result", {}).get("data", [])[:5]
    
    news_list = ["【今日金融热点】"]
    for idx, news in enumerate(news_data, 1):
        news_list.append(f"{idx}. {news.get('title', '无标题新闻')}")
    
    return "\n".join(news_list) if news_list else "今日暂无更新"

def send_to_wechat(content):
    requests.post(
        f"https://sctapi.ftqq.com/{SEND_KEY}.send",
        data={"text": "金融早报推送", "desp": content}
    )

if __name__ == "__main__":
    news_content = get_financial_news()
    send_to_wechat(news_content)
