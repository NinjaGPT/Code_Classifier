import os, warnings

from langchain.agents.agent_toolkits import create_python_agent
from langchain.agents import load_tools, initialize_agent
from langchain.agents import AgentType
from langchain.tools.python.tool import PythonREPLTool
from langchain.python import PythonREPL
from langchain.chat_models import ChatOpenAI

# langchain==0.0.250
warnings.filterwarnings("ignore")
os.environ['OPENAI_API_KEY'] = 'sk-XX'

llm = ChatOpenAI(temperature=0)

tools = load_tools(["llm-math", "wikipedia"], llm=llm)

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
    verbose=True)

# LLM-MATH
# agent("What is the 20% of 1000?")

# WIKIPEDIA
question = "who is lulzSec?"
print(agent(question))

