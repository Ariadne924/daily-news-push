import requests
SEND_KEY = "SCT340534Tzruc1Oeqj2q71uLgXPp34n8s"

def get_news():
    # 抓取金融早报
    finance = requests.get("https://api.jinrishici.com/v1/getFinanceNews", timeout=10).json()["data"][:5]
    # 抓取教育资讯
    edu = requests.get("https://api.jinrishici.com/v1/getEduNews", timeout=10).json()["data"][:3]
    # 合并内容
    news = ["【今日金融早报】"] + [f"{i+1}. {n['title']}" for i,n in enumerate(finance)]
    news += ["\n【教育资讯更新】"] + [f"{i+1}. {n['title']}" for i,n in enumerate(edu)]
    return "\n".join(news)

requests.get(f"https://sctapi.ftqq.com/{SEND_KEY}.send?title=每日财经&desp={get_news()}")
