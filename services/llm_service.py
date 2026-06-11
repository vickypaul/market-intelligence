import os
import json
import re
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class LLMService:

    def __init__(
        self,
        provider="openai"
    ):

        if provider == "openai":

            self.client = OpenAI(
                api_key=os.getenv("OPENAI_API_KEY")
            )

            self.model = "gpt-4.1-mini"

        else:

            self.client = OpenAI(
                api_key=os.getenv("VLLM_API_KEY"),
                base_url=os.getenv("VLLM_BASE_URL")
            )

            self.model = "Qwen/Qwen3-8B"

    def analyze(
        self,
        news_chunk,
        prompt
    ):

        final_prompt = prompt.replace(
            "{news}",
            news_chunk
        )

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=0.2,
            messages=[
                {
                    "role": "user",
                    "content": final_prompt
                }
            ]
        )
        content = response.choices[0].message.content

        # Try to extract a JSON object from the model output.
        # Remove common markdown fences and language tags first.
        cleaned = content.replace('```json', '').replace('```', '')

        # Find the first { and last } to get the JSON substring.
        start = cleaned.find('{')
        end = cleaned.rfind('}')

        if start != -1 and end != -1 and end > start:
            candidate = cleaned[start:end+1]

            try:
                return json.loads(candidate)
            except json.JSONDecodeError:
                # Try to fix common issues like trailing commas.
                candidate_fixed = re.sub(r',(\s*[}\]])', r'\1', candidate)
                try:
                    return json.loads(candidate_fixed)
                except json.JSONDecodeError:
                    # Fall back to returning raw content when parsing fails.
                    return content

        # No obvious JSON found — return raw content.
        return content