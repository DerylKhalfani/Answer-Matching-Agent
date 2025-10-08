import os
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages


# Structured Output for Agent State
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]