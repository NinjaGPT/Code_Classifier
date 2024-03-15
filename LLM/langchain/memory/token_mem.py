import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationTokenBufferMemory
from langchain.llms import OpenAI


def __init_env__():
    os.environ['OPENAI_API_KEY'] = 'sk-XX'

__init_env__()
llm = ChatOpenAI(temperature=0.0)
memory = ConversationTokenBufferMemory(llm=llm, max_token_limit=30) # the numbers of tokens

memory.save_context({"input":"AI is what?"},{"output":"Amazing!"})
memory.save_context({"input":"Backpropagation is what?"},{"output":"Beautiful!"})
memory.save_context({"input":"Chatbot is what?"},{"output":"Charming!"})
print(memory.load_memory_variables({}))
