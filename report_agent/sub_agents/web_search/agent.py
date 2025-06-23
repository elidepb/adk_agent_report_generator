from google.adk.agents import Agent
from google.adk.tools import google_search
from . import prompt

MODEL = "gemini-2.5-pro"

web_search_agent = Agent(
    name="web_search_agent",
    model=MODEL,
    instruction=prompt.WEB_SEARCH_PROMPT,
    tools=[google_search],
)