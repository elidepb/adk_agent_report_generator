from google.adk.agents import LlmAgent
from . import prompt

MODEL = "gemini-2.5-pro"

style_analisis_agent = LlmAgent(
    name="style_analisis_agent",
    model=MODEL,
    description="Expert agent that analyzes a sample text and extracts its stylistic characteristics (tone, formality, etc.) into a structured format.",
    instruction=prompt.STYLE_ANALISIS_PROMPT,
)