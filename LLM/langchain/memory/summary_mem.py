from langchain.memory import ConversationSummaryBufferMemory
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
import os

def __init_env__():
    os.environ['OPENAI_API_KEY'] = 'sk-XX'

__init_env__()

schedule = "there is a meeting at 8 am with your product team, \
    you will need your PPT presentation prepared. \
    9am-12pm have time to work on your langchain \
    project which will go quickly because langchain is such a powerful tool. \
    At Noon, lunch at the italian resturant with a customer who is driving\
    from over an hour away to meet you to understand the latest in AI.\
    be sure to bring your laptop to show the latest LLM demo."
llm = ChatOpenAI(temperature=0.0)
memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=100)
memory.save_context({"input":"Hi AI"},{"output":"what's up"})
memory.save_context({"input":"not much, just hanging"},{"output":"cool"})
memory.save_context({"input":"what is on the schedule today?"},{"output":f"{schedule}"})

print(memory.load_memory_variables({}))
# when the max_token_limit=400
# labs :: 0xPecker/langchain/memory 1 » python3 summary_mem.py
# {'history': "Human: Hi AI\nAI: what's up\nHuman: not much, just hanging\nAI: cool\nHuman: what is on the schedule today?\nAI: there is a meeting at 8 am with your product team,     you will need your PPT presentation prepared.     9am-12pm have time to work on your langchain     project which will go quickly because langchain is such a powerful tool.     At Noon, lunch at the italian resturant with a customer who is driving    from over an hour away to meet you to understand the latest in AI.    be sure to bring your laptop to show the latest LLM demo."}

# when the max_token_limit=100
# labs :: 0xPecker/langchain/memory » python3 summary_mem.py
# {'history': 'System: The human and AI engage in a casual conversation. The human asks about the schedule for the day, and the AI provides a detailed plan including a meeting with the product team, working on the langchain project, and a lunch meeting with a customer interested in AI. The AI emphasizes the importance of bringing a laptop to showcase the latest LLM demo during the lunch meeting.'}


conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

print(conversation.predict(input="what would be a good demo to show?"))
#print(memory.load_memory_variables({}))
