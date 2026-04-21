import requests
SEND_KEY = "SCT340534Tzruc1Oeqj2q71uLgXPp34n8s"

def get_news():
    finance = requests.get("https://api.vvhan.com/api/news?type=finance&page=1", timeout=10).json()["data"][:5]
  
    edu = requests.get("https://api.vvhan.com/api/news?type=edu&page=1", timeout=10).json()["data"][:3]
    news = ["【今日金融早报】"] + [f"{i+1}. {n['title']}" for i,n in enumerate(finance)]
    news += ["\n【教育资讯更新】"] + [f"{i+1}. {n['title']}" for i,n in enumerate(edu)]
    return "\n".join(news)

requests.get(f"https://sctapi.ftqq.com/{SEND_KEY}.send?title=每日财经&desp={get_news()}")
