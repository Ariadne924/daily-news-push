import requests

KEY = "SCT340534Tkb8yYcTXtIjOkOBKHNK7EQTw"

def get_data():
    try:
        headers = {"User-Agent":"Mozilla/5.0"}
        r = requests.get("https://api.thenewsapi.com/v1/news/top?api_key=demo&language=zh", headers=headers, timeout=15)
        j = r.json()
        res = ["📊 今日财经&热点新闻"]
        for item in j.get("data", [])[:6]:
            res.append(f"{item['title']}")
        return "\n\n".join(res)
    except:
        return "接口访问受限"

requests.post(f"https://sctapi.ftqq.com/{KEY}.send",
json={"text":"每日新闻推送","desp":get_data()})
