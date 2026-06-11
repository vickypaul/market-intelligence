from pathlib import Path

from services.llm_service import LLMService


def analyze_chunks(chunks):

    prompt = Path(
        "prompts/market_prompt.txt"
    ).read_text(
        encoding="utf-8"
    )

    llm = LLMService(
        provider="openai"
    )

    results = []

    for index, chunk in enumerate(chunks):

        print(
            f"Analyzing chunk {index+1}/{len(chunks)}"
        )

        result = llm.analyze(
            chunk,
            prompt
        )

        results.append(result)

    return results