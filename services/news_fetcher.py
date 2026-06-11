# services/news_fetcher.py

import feedparser
import json
from pathlib import Path
from services.article_extractor import extract_article


RSS_FEEDS = [
    "https://economictimes.indiatimes.com/rssfeedsdefault.cms"
]


def fetch_news():

    all_news = []

    for feed_url in RSS_FEEDS:

        feed = feedparser.parse(feed_url)

        for entry in feed.entries:

            article_data = extract_article(
                entry.get("link", "")
            )

            all_news.append(
                {
                    "title": entry.get("title", ""),
                    "link": entry.get("link", ""),
                    "published": entry.get("published", ""),
                    "summary": entry.get("summary", ""),
                    "content": article_data["text"]
                }
            )

    return all_news


def save_news(news):

    Path("data/raw_news").mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        "data/raw_news/news.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            news,
            f,
            indent=2,
            ensure_ascii=False
        )