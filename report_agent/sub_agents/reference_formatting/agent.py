from google.adk.agents import LlmAgent
from . import prompt

MODEL = "gemini-2.5-pro"

reference_formatting_agent = LlmAgent(
    name="reference_formatting_agent",
    model=MODEL,
    description="Expert agent that receives a list of URLs and a style format (e.g. APA) and returns a formatted bibliography.",
    instruction=prompt.REFERENCE_FORMATTING_PROMPT,
)