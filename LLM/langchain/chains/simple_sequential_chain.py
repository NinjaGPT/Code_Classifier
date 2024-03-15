import os
import pandas as pd
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate
from langchain.chains import SimpleSequentialChain

def __init_env__():
    os.environ['OPENAI_API_KEY'] = 'sk-XX'

__init_env__()

# df = pd.read_csv('data.csv')
# print(df.head())

product = "LLM based vulnerability analysis and exploitation"
llm = ChatOpenAI(temperature=0.9)

first_prompt = ChatPromptTemplate.from_template("what is the best name to describe a company that makes {product}?")
chain_one = LLMChain(llm=llm, prompt=first_prompt)
 
second_prompt = ChatPromptTemplate.from_template("write a 20 words description for the following company: {company_name}?")
chain_two = LLMChain(llm=llm, prompt=second_prompt)

overall_simple_chain = SimpleSequentialChain(chains=[chain_one, chain_two], verbose=True)

print(overall_simple_chain.run(product))
