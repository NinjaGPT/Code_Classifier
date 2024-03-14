import os
from langchain.agents import tool
from datetime import date
# from langchain.agents.agent_toolkits import create_python_agent
from langchain.agents import load_tools, initialize_agent
from langchain.agents import AgentType
from langchain.tools.python.tool import PythonREPLTool
# from langchain.python import PythonREPL
from langchain.chat_models import ChatOpenAI

# langchain==0.0.250
os.environ['OPENAI_API_KEY'] = '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'

llm = ChatOpenAI(temperature=0)

@tool
def time(text: str) -> str:
    """Returns todays date, use this for any questions related to knowing todays date.\
    The input should always be an empty string, and this function will always return todays\
    date - any date mathmatics should occur outside this function."""
    return str(date.today())

tools = load_tools(["llm-math", "wikipedia"], llm=llm)

agent = initialize_agent(
     tools + [time],
     llm,
     agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
     handle_parsing_errors=True,
     verbose=True
 )



agent.run("whats the date today?")