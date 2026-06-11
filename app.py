import streamlit as st

from services.news_fetcher import fetch_news, save_news
from services.chunker import chunk_news, save_chunks
from services.news_fetcher import (
    fetch_news,
    save_news
)

from services.chunker import (
    chunk_news,
    save_chunks
)

from services.analyzer import (
    analyze_chunks
)

from services.report_service import (
    save_report
)

st.title("📈 Market Intelligence Engine")

if st.button("Analyze Market"):

    with st.spinner("Fetching News..."):

        news = fetch_news()

        save_news(news)

    st.success(f"Fetched {len(news)} articles")

    with st.spinner("Generating Chunks..."):

        chunks = chunk_news(news)

        save_chunks(chunks)

    with st.spinner("Fetching News..."):

        news = fetch_news()

        save_news(news)

    with st.spinner("Chunking News..."):

        chunks = chunk_news(news)

        save_chunks(chunks)

    with st.spinner("Running AI Analysis..."):

        results = analyze_chunks(
            chunks
        )

    for index, result in enumerate(results):

        with st.expander(
            f"Chunk {index+1}"
        ):
            st.json(result)

        save_report(results)

    st.success("Analysis Complete")

    st.success(f"Generated {len(chunks)} chunks")

    st.write("Pipeline completed successfully")

    st.metric("Articles Fetched", len(news))
    st.metric("Chunks Generated", len(chunks))