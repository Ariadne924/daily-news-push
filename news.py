import requests
SEND_KEY = "SCT340534Tzruc1Oeqj2q71uLgXPp34n8s"

def get_news():
    finance = requests.get("https://www.cls.cn/api/sw?app=CailianpressWeb&os=web&sv=7.7.5&action=getRollingNews&lastTime=0&lastId=0&pageSize=5&channel=finance", timeout=10).json()["data"]["roll_news"][:5]
    
    edu = requests.get("https://www.cls.cn/api/sw?app=CailianpressWeb&os=web&sv=7.7.5&action=getRollingNews&lastTime=0&lastId=0&pageSize=3&channel=education", timeout=10).json()["data"]["roll_news"][:3]
    news = ["【今日金融早报】"] + [f"{i+1}. {n['title']}" for i,n in enumerate(finance)]
    news += ["\n【教育资讯更新】"] + [f"{i+1}. {n['title']}" for i,n in enumerate(edu)]
    return "\n".join(news)

requests.get(f"https://sctapi.ftqq.com/{SEND_KEY}.send?title=每日财经&desp={get_news()}")
