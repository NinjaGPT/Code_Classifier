from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import openai
import os

def __init_env__():
    os.environ['OPENAI_API_KEY'] = 'sk-XX'

template_string = """
Translate the text \
that is delimited by triple backticks \
into a style that is {style}. \
text: ```{text}```
"""
customer_email = """
你好，我是克里斯，我想试试这个函数。
"""

customer_style = """
American English in a calm and respectful tone
"""

prompt_template = ChatPromptTemplate.from_template(template_string)

customer_messages = prompt_template.format_messages(
    style=customer_style,
    text=customer_email
)
__init_env__()
chat = ChatOpenAI(temperature=0.0)

customer_response = chat(customer_messages)
# print(prompt_template.messages[0].prompt)
# chat = ChatOpenAI(temperature=0.0)
print(customer_response.content)
