from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from ..web_search import web_search_agent
from . import prompt

MODEL = "gemini-2.5-pro"

writing_agent = LlmAgent(
    name="writing_agent",
    model=MODEL,
    description=("An agent skilled in researching and writing the detailed content of a single section of a report, based on a title and summary."),
    instruction=prompt.WRITING_PROMPT,
    tools=[
        AgentTool(agent=web_search_agent),
    ]
)