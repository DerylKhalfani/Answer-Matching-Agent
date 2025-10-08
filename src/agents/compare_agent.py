from components.state import State
from langchain.chat_models import init_chat_model

llm = init_chat_model("openai:gpt-4o-mini")

def compare_agent(state: State) -> State:

    return {"messages": [llm.invoke(state["messages"])]}