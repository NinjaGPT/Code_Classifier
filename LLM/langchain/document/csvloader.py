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

index = VectorstoreIndexCreator(vectorstore_cls=DocArrayInMemorySearch).from_loaders([loader])

query = "please list all your shirts with sun protection in a table in markdown and summarize each one."
response = index.query(query)

display(Markdown(response))
# will occur an error:
# openai.error.InvalidRequestError: The model `text-davinci-003` has been deprecated
