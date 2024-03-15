from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import CSVLoader
from langchain.vectorstores import DocArrayInMemorySearch
from IPython.display import display, Markdown
from langchain.indexes import VectorstoreIndexCreator
from langchain.embeddings import OpenAIEmbeddings
import os

os.environ['OPENAI_API_KEY'] = 'sk-XX'


file = 'ok.csv'
loader = CSVLoader(file_path=file)

docs = loader.load()
print(docs[0].metadata)
print(docs[0].page_content)
print("-" * 90)
embeddings = OpenAIEmbeddings()
embed = embeddings.embed_query("Hi my name is Chris!")    # create embedding
print(len(embed),"vectors")
print(embed[:5])
print("-" * 90)

db = DocArrayInMemorySearch.from_documents(docs, embeddings)

query = "please suggest a lady's name"

docs = db.similarity_search(query)
print(docs[0])
#print(list(docs))
print("length:",len(docs))

retriever = db.as_retriever()
llm = ChatOpenAI(temperature=0)
qdocs = "".join([docs[i].page_content for i in range(len(docs))])

response = llm.call_as_llm(f"{qdocs} Question: please list all lady's names in a cable in markdown and expain each one")
#display(Markdown(response))
print(response)
print("-" * 90)
qa_stuff = RetrievalQA.from_chain_type(
    llm=llm,                
    chain_type="stuff",      
    retriever=retriever,
    verbose=True)
#res = index.query(query, llm=llm)
q = "please list all lady's names in a cable in markdown and expain each one"
res = qa_stuff.run(q)
#display(Markdown(res))
print(res)

#################### Chain Types ####################
# stuff: put question in prompt and get answer.
# Map_reduce: every chunk's content with question transfer to LLM then get a singel result, LLM will summary them.
# Refine: each chunk's output as next chunk's input.
# Map_rerank: every chunk's content with question transfer to LLM then get a singel result and score, LLM will choose highest one.
