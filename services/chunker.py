import json
from pathlib import Path

def chunk_news(
    articles,
    max_chars=12000
):

    chunks = []

    current_chunk = ""

    for article in articles:

        text = f"""

TITLE:
{article['title']}

CONTENT:
{article['content']}

--------------------
"""

        if len(current_chunk) + len(text) > max_chars:

            chunks.append(current_chunk)

            current_chunk = text

        else:

            current_chunk += text

    if current_chunk:
        chunks.append(current_chunk)

    return chunks

def save_chunks(chunks):

    Path(
        "data/processed_news"
    ).mkdir(
        parents=True,
        exist_ok=True
    )

    for idx, chunk in enumerate(chunks):

        with open(
            f"data/processed_news/chunk_{idx}.txt",
            "w",
            encoding="utf-8"
        ) as f:

            f.write(chunk)