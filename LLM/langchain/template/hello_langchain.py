import openai
import os

os.environ['OPENAI_API_KEY'] = 'sk-XX'
openai.api_key = os.environ['OPENAI_API_KEY']

def get_completion(prompt, model="gpt-4-1106-preview"):
    messages = [{"role":"user","content":prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]



customer_email = """
你好，我是克里斯，我想试试这个函数。
"""

style = """
American English in a calm and respectful tone
"""
prompt = f"""
Translate the text that is delimited by triple \
backticks into a style that is {style}.
text:```{customer_email}```
"""

response = get_completion(prompt)
print(response)
