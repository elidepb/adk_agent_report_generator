from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from ..writing import writing_agent
from ..reference_formatting import reference_formatting_agent
from . import prompt

MODEL = "gemini-2.5-pro"

report_builder_agent = LlmAgent(
    name="report_builder_agent",
    model=MODEL,
    description="Directing agent who takes an approved index and uses other agents to write, format references, and assemble the complete final report.",
    instruction=prompt.REPORT_BUILDER_PROMPT,
    tools=[
        AgentTool(agent=writing_agent),
        AgentTool(agent=reference_formatting_agent),
    ]
)