from google.adk.agents import LlmAgent
from . import prompt

MODEL = "gemini-2.5-pro"

translation_agent = LlmAgent(
    name="translation_agent",
    model=MODEL,
    description="Expert agent that receives a block of text and a target language, and returns the fully translated text.",
    instruction=prompt.TRANSLATION_PROMPT,
)