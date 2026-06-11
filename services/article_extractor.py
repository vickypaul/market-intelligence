try:
    from newspaper import Article

    def extract_article(url):
        try:
            article = Article(url)
            article.download()
            article.parse()

            return {
                "text": article.text,
                "authors": article.authors,
                "publish_date": str(article.publish_date)
            }
        except Exception as e:
            print(f"Error (newspaper): {url} -> {e}")
            return {
                "text": "",
                "authors": [],
                "publish_date": None
            }
except Exception:
    import requests
    from bs4 import BeautifulSoup

    def extract_article(url):
        try:
            if not url:
                return {"text": "", "authors": [], "publish_date": None}

            resp = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
            resp.raise_for_status()

            # Prefer lxml if available, otherwise fall back to the built-in parser
            try:
                import lxml  # noqa: F401
                bs_parser = "lxml"
            except Exception:
                bs_parser = "html.parser"

            soup = BeautifulSoup(resp.text, bs_parser)

            article_tag = soup.find("article")
            if article_tag:
                paragraphs = [p.get_text(strip=True) for p in article_tag.find_all("p")]
            else:
                paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]

            text = "\n\n".join([p for p in paragraphs if p])

            return {"text": text, "authors": [], "publish_date": None}
        except Exception as e:
            print(f"Error (bs4): {url} -> {e}")
            return {"text": "", "authors": [], "publish_date": None}