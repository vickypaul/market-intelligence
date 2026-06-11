from services.news_fetcher import fetch_news

news = fetch_news()

print(news[0]["title"])

print(news[0]["content"][:1000])