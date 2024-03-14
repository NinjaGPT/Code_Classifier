import os, warnings

from langchain.agents.agent_toolkits import create_python_agent
from langchain.agents import load_tools, initialize_agent
from langchain.agents import AgentType
from langchain.tools.python.tool import PythonREPLTool
from langchain.python import PythonREPL
from langchain.chat_models import ChatOpenAI

# langchain==0.0.250
warnings.filterwarnings("ignore")
os.environ['OPENAI_API_KEY'] = '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'

llm = ChatOpenAI(temperature=0)

agent = create_python_agent(
    tool=PythonREPLTool(),llm=llm)

customer_list = [
    ["Geoff", "Fusion"],
    ["Jen", "Ayai"],
    ["Dolly", "Too"],
    ["Elle", "Elem"]
] 

agent.run(f"Sort these customers by last name and then first name and print the output: {customer_list}")
