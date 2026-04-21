import requests
SEND_KEY = "SCT340534Tzruc1Oeqj2q71uLgXPp34n8s"
requests.get(f"https://sctapi.ftqq.com/{SEND_KEY}.send?title=测试&desp=终于通了！")
