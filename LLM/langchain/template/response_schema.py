import os, openai
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser


def __init_env__():
    os.environ['OPENAI_API_KEY'] = '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'



gift_schema = ResponseSchema(name="gift", description="Was the item purchased as a gift for someone else? Answer True if yes, False if not or unknown.")
delivery_days_schema = ResponseSchema(name="delivery_days", description="How many days did it take for the product to arrive? If this information is not found, output -1.")
price_value_schema = ResponseSchema(name="price_value", description="Extract any sentences about the value or price, and output them as a comma separated python list.")

response_schema = [gift_schema, delivery_days_schema, price_value_schema]

parser = StructuredOutputParser(response_schemas=response_schema)

# Now you can use the parser as intended
format_instructions = parser.get_format_instructions()
# print(format_instructions)

review_template_2 = """
For the following text, extract the following information:

gift: Was the item purchased as a gift for someone else? Answer True if yes, False if not or unknown.
delivery_days: How many days did it take for the product to arrive? If this information is not found, output -1.
price_value: Extract any sentences about the value or price, and output them as a comma separated python list.

text: {text}
{format_instructions}
"""
customer_review = "xxxx"
prompt = ChatPromptTemplate.from_template(template=review_template_2)
messages = prompt.format_messages(text=customer_review, format_instructions=format_instructions)
#print(messages[0].content)
__init_env__()
chat = ChatOpenAI(temperature=0.0)
response = chat(messages)
print(response.content)

output_dict = parser.parse(response.content)
print(type(output_dict))