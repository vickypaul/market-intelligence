import streamlit as st

from services.news_fetcher import fetch_news, save_news
from services.chunker import chunk_news, save_chunks
from services.analyzer import analyze_chunks
from services.report_service import save_report


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Market Intelligence Engine",
    page_icon="📈",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.hero-card {
    background: linear-gradient(135deg,#111827,#1f2937);
    padding: 30px;
    border-radius: 20px;
    border: 1px solid #2d3748;
    margin-bottom: 20px;
}

.hero-title {
    font-size: 40px;
    font-weight: 700;
    color: white;
}

.hero-subtitle {
    color: #9ca3af;
    font-size: 16px;
}

.metric-card {
    background-color:#1A1D24;
    padding:20px;
    border-radius:15px;
    border:1px solid #2d3748;
    text-align:center;
}

.metric-value {
    font-size:30px;
    font-weight:bold;
    color:#00C2FF;
}

.metric-label {
    color:#9ca3af;
}

.block-container {
    padding-top: 1rem;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HERO SECTION
# =====================================================

st.markdown("""
<div class="hero-card">
    <div class="hero-title">
        🇮🇳 Indian Market Intelligence Engine
    </div>
    <div class="hero-subtitle">
        Institutional Grade Market Intelligence Powered by AMD ROCm + vLLM
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================================
# BUTTON
# =====================================================

analyze_clicked = st.button(
    "🚀 Analyze Market",
    use_container_width=True
)

# =====================================================
# DEFAULT SCREEN
# =====================================================

if not analyze_clicked:

    st.info(
        "Click Analyze Market to generate intelligence from latest market news."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        ### 📡 News Sources

        - Moneycontrol
        - Economic Times
        - LiveMint
        - Business Standard
        """)

    with col2:
        st.markdown("""
        ### 🧠 AI Engine

        - OpenAI
        - AMD ROCm
        - vLLM
        - Chunk Analysis
        """)

    with col3:
        st.markdown("""
        ### 📈 Upcoming

        - Risk Detection
        - Opportunity Detection
        - Narrative Detection
        - Sector Rotation
        """)

# =====================================================
# PIPELINE
# =====================================================

else:

    progress = st.progress(0)

    with st.spinner("Fetching market news..."):

        news = fetch_news()
        save_news(news)

    progress.progress(25)

    with st.spinner("Generating chunks..."):

        chunks = chunk_news(news)
        save_chunks(chunks)

    progress.progress(50)

    with st.spinner("Running AI analysis..."):

        results = analyze_chunks(chunks)

        save_report(results)

    progress.progress(100)

    st.success("Analysis Complete")

    # =================================================
    # DASHBOARD METRICS
    # =================================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{len(news)}</div>
            <div class="metric-label">Articles</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{len(chunks)}</div>
            <div class="metric-label">Chunks</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">AI</div>
            <div class="metric-label">Analysis</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">✓</div>
            <div class="metric-label">Status</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # =================================================
    # TABS
    # =================================================

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📋 Executive Summary",
        "⚠ Risks",
        "💰 Opportunities",
        "🏭 Sectors",
        "🔍 Raw Analysis"
    ])

    with tab1:

        st.subheader("Executive Summary")

        st.success(
            "Meta-analysis engine will populate this section in the next phase."
        )

    with tab2:

        st.subheader("Key Risks")

        st.info(
            "Risk detection coming soon."
        )

    with tab3:

        st.subheader("Opportunities")

        st.info(
            "Opportunity extraction coming soon."
        )

    with tab4:

        st.subheader("Sector Intelligence")

        st.info(
            "Sector rotation analysis coming soon."
        )

    with tab5:

        st.subheader("Chunk Analysis")

        for idx, result in enumerate(results):

            with st.expander(
                f"Chunk {idx+1}"
            ):

                try:
                    st.json(result)
                except:
                    st.write(result)