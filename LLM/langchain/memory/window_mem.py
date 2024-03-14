from langchain.memory import ConversationBufferWindowMemory

memory = ConversationBufferWindowMemory(k=1)    # last round of talks

memory.save_context({"input":"Hi AI"},{"output":"what's up"})
memory.save_context({"input":"not much, just hanging"},{"output":"cool"})

print(memory.load_memory_variables({}))