import os
import httpx
from dotenv import load_dotenv

load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"
MISTRAL_MODEL = "mistral-small"

headers = {
    "Authorization": f"Bearer {MISTRAL_API_KEY}",
    "Content-Type": "application/json"
}

def analyze_text_with_llm(prompt: str) -> str:
    payload = {
        "model": MISTRAL_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2
    }

    try:
        response = httpx.post(
            MISTRAL_API_URL,
            headers=headers,
            json=payload,
            timeout=60.0  # 🔥 extended timeout from default ~10s
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    
    except httpx.TimeoutException:
        return "LLM API call failed: The request timed out (even with 60s limit). Mistral may be slow or overloaded."

    except httpx.HTTPStatusError as http_err:
        return f"[HTTP Error] {http_err.response.status_code}: {http_err.response.text}"

    except Exception as e:
        return f"[General Error] {str(e)}"

