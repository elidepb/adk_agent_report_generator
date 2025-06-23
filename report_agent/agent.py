from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .sub_agents.outline import outline_agent
from .sub_agents.report_builder import report_builder_agent
from .sub_agents.translation import translation_agent
from .sub_agents.style_analysis import style_analisis_agent

from .sub_agents.pdf_generator.agent import create_professional_pdf

MODEL = "gemini-2.5-pro"

pdf_creation_tool = FunctionTool(create_professional_pdf)

coordinator = LlmAgent(
    name="coordinator",
    model=MODEL,
    description=("Main agent that receives the user's request and delegates tasks to specialist sub-agents."),
    instruction=prompt.COORDINATOR_PROMPT,
    tools=[
        AgentTool(agent=outline_agent),
        AgentTool(agent=report_builder_agent),
        AgentTool(agent=translation_agent),
        AgentTool(agent=style_analisis_agent),
        pdf_creation_tool,
    ]
)

root_agent = coordinator