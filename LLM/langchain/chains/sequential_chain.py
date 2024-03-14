import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate
from langchain.chains import SequentialChain
import pandas as pd

def __init_env__():
    os.environ['OPENAI_API_KEY'] = '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'

__init_env__()

llm = ChatOpenAI(temperature=0.9)

first_prompt = ChatPromptTemplate.from_template("translate the following review to english: {Review}")
chain_one = LLMChain(llm=llm, prompt=first_prompt, output_key="English_Review")
 
second_prompt = ChatPromptTemplate.from_template("can you summarize the following review in 1 sentence: {English_Review}?")
chain_two = LLMChain(llm=llm, prompt=second_prompt, output_key="summary")

third_prompt = ChatPromptTemplate.from_template("what language is the following review: {Review}")
chain_three = LLMChain(llm=llm, prompt=third_prompt, output_key="language")
 
fourth_prompt = ChatPromptTemplate.from_template("write a follow up response to the following "
                                                  "summary in the specified language:"
                                                  "\n\nSummary: {summary}\n\nLanguage: {language}"
                                                  )
chain_four = LLMChain(llm=llm, prompt=fourth_prompt, output_key="followup_message")

overall_chain = SequentialChain(
    chains=[chain_one, chain_two, chain_three, chain_four],
    input_variables=["Review"],
    output_variables=["English_Review", "summary","language","followup_message"],
    verbose=True
)

Review = "这个产品用起来还可以，但是质量还有待提高"
print(overall_chain(Review))

# df = pd.read_csv('data.csv')
# review = df.Review[1]

