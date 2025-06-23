from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from ..web_search import web_search_agent
from . import prompt

MODEL = "gemini-2.5-pro"

outline_agent = LlmAgent(
    name="outline_agent",
    model=MODEL,
    description=("Expert agent in researching a topic and proposing a detailed table of contents with summaries for a report."),
    instruction=prompt.OUTLINE_PROMPT,
    tools=[
        AgentTool(agent=web_search_agent),
    ]
)