import requests
from langchain.llms.base import LLM
from pydantic import BaseModel, Field

class OllamaLLM(LLM, BaseModel):
    """Custom LLM wrapper for Ollama."""

    model: str = Field(default="llama3.1:8b")
    api_url: str = Field(default="http://127.0.0.1:11434/api/generate")

    @property
    def _llm_type(self) -> str:
        return "ollama"

    def _call(self, prompt: str, stop=None) -> str:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "stop": stop or []
        }
        response = requests.post(self.api_url, json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "")

    def generate(self, prompt: str) -> str:
        """Convenience method to directly get the response."""
        return self._call(prompt)
