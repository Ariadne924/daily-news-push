import requests

SERVERCHAN_KEY = "SCT340534Tkb8yYcTXtIjOkOBKHNK7EQTw"

def get_daily_news():
    try:
        resp = requests.get("https://api.vvhan.com/api/60s?type=json", timeout=15)
        resp.raise_for_status()
        res = resp.json()
        if res.get("success") and "data" in res:
            news_body = ["📢 今日财经&热点早间播报\n"]
            for index, single_news in enumerate(res["data"]["news"][:8], 1):
                news_body.append(f"{index}. {single_news}")
            return "\n".join(news_body)
        return "今日新闻暂未更新，请稍后重试"
    except Exception as e:
        return f"新闻获取临时异常，错误详情：{str(e)}"

def send_to_wechat(news_text):
    try:
        push_url = f"https://sctapi.ftqq.com/{SERVERCHAN_KEY}.send"
        push_data = {"text": "✨ 每日新闻自动推送", "desp": news_text}
        requests.post(push_url, data=push_data, timeout=10)
    except:
        pass

if __name__ == "__main__":
    final_content = get_daily_news()
    send_to_wechat(final_content)
