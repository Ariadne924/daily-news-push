import requests
SEND_KEY = "你的SendKey"
requests.get(f"https://sctapi.ftqq.com/{SEND_KEY}.send?title=测试&desp=终于通了！")
