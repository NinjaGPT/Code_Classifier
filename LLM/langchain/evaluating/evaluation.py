import os, langchain, warnings
from IPython.display import display, Markdown
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import CSVLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.vectorstores import DocArrayInMemorySearch
from langchain.evaluation.qa import QAGenerateChain
from langchain.evaluation.qa import QAEvalChain

os.environ['OPENAI_API_KEY'] = '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'
#langchain.debug = True
warnings.filterwarnings("ignore")

file = 'data.csv'
loader = CSVLoader(file_path=file)
data = loader.load()
# create a index
index = VectorstoreIndexCreator(vectorstore_cls=DocArrayInMemorySearch).from_loaders([loader])

llm = ChatOpenAI(temperature=0)
qa = RetrievalQA.from_chain_type(
    llm=llm,                
    chain_type="stuff",      
    retriever=index.vectorstore.as_retriever(),
    verbose=True,
    chain_type_kwargs = {
        "document_separator":"<<<<>>>>>"
    })
examples = [
    {
        "query": "what is chris' height?",
        "answer": "175cm"
    }
]

print(data[1])  # second row, tiffany
print("-" * 90)
# generate question and answer pair
example_gen_chain = QAGenerateChain.from_llm(ChatOpenAI())
new_examples = example_gen_chain.apply_and_parse(
    [{"doc": t} for t in data[:3]]
    )
print(" THIS IS NEW EXAMPLES:")

print(new_examples[1]['qa_pairs'])
print("-" * 90)
examples += new_examples 
print(qa.run(new_examples[0]["qa_pairs"]))

predictions = qa.apply(new_examples[0]["qa_pairs"]["query"])    # the list of answers

eval_chain = QAEvalChain.from_llm(llm)  
graded_outputs = eval_chain.evaluate(examples, predictions)  # evaluate

for i, eg in enumerate(examples):
    print(f"Example {i};")
    print("Question: " + predictions[i]['query'])           # question generated from LLM
    print("Real Answer: " + predictions[i]['answer'])       # answer generated from LLM
    print("Predicted Answer: " + predictions[i]['result'])  # retrieval with the embedding in the vector DB, passing that into LLM, guess answer
    print("Predicted Grade: " + graded_outputs[i]['text'])  # score from LLM
    print()
