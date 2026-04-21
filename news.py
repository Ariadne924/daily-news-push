import requests

# ========== 这里换成你刚才复制的 Server酱 SendKey ==========
SEND_KEY = "SCT340534Tzruc1Oeqj2q71uLgXPp34n8s"
# ========================================================

# 获取每日新闻
def get_news():
    return ["测试新闻1：今天天气不错", "测试新闻2：祝推送成功"]

# 推送到微信
def wechat_push(content):
    title = "📰 每日新闻速览"
    desp = "\n\n".join([f"{i+1}. {txt}" for i, txt in enumerate(content)])
    push_url = f"https://sctapi.ftqq.com/{SEND_KEY}.send?title={title}&desp={desp}"
    requests.get(push_url)

if __name__ == "__main__":
    news_list = get_news()
    wechat_push(news_list)
