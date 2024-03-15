import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

def __init_env__():
    os.environ['OPENAI_API_KEY'] = 'sk-XX'

__init_env__()

llm = ChatOpenAI(temperature=0.0)
memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=False
)

 
print(conversation.predict(input="Hi, my name is Chris"))
print(conversation.predict(input="what is 2**10?"))
print(conversation.predict(input="Hi, what's my  name?"))

memory.save_context({"input":"Hi GPT4!"},{"output":"what's up?"})

print("-" * 90)
print("Memory Buffer:")
print("-" * 90)

print(f"{memory.buffer}\n","-" * 90,"\n")
print(memory.load_memory_variables({}))
