# test_chunker.py

from services.news_fetcher import fetch_news
from services.chunker import chunk_news

news = fetch_news()

chunks = chunk_news(news)

print("Chunks:", len(chunks))

print(chunks[0][:1000])