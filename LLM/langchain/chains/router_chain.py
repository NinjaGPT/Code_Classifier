import os, warnings
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.chains.router import MultiPromptChain
from langchain.chains.router.llm_router import LLMRouterChain, RouterOutputParser
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate

warnings.filterwarnings("ignore")
"""
MultiPromptChain - routing between different prompt templates
LLMRouterChain - routing between different sub-chains
RouterOutputParser - parse the Output of LLM as dictionary
PromptTemplate - 
"""

physics_template = """
you are a very smart physics professor,
you are great at answering questions about physics in a
when you do not know the answer to a question you admit that

here is a question:
{input}
"""

math_template = """
you are a very good mathematician, you are
you are so good because you are able to break down hard pro
answer the component parts, and then put them together to

here is a question:
{input}
"""

history_template = """
you are a very good historian. you ha
contexts from a range of historical periods. you have the a
evaluate the past. you have a respect for historical eviden
your explanations and judgements.

here is a question:
{input}
"""

computerscience_template = """
you are a successful computer scientist. you have a passion
forward-thinking, confidence, strong problem-solving capability
and excellent communication skills. you are great at answer
you are so good bacause you know how to solve a problem by
that a machine can easily interpret and you know how to ch
time complexity and space complexity

here is a question:
{input}
"""

prompt_infos = [


    {
        "name":"physics",
        "description":"good for answering questions about physics",
        "prompt_template": physics_template
    },
    {
        "name":"math",
        "description":"good for answering questions about math",
        "prompt_template": math_template
    },
    {
        "name":"history",
        "description":"good for answering questions about history",
        "prompt_template": history_template
    },
    {
        "name":"computer science",
        "description":"good for answering questions about computer science",
        "prompt_template": computerscience_template
    }
]

def __init_env__():
    os.environ['OPENAI_API_KEY'] = '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'
__init_env__()
# instance object of ChatGPT
llm = ChatOpenAI(temperature=0)     

# destination chains =====================================
destination_chains = {}
for p_info in prompt_infos:         
    name = p_info["name"]
    prompt_template = p_info["prompt_template"]
    prompt = ChatPromptTemplate.from_template(template=prompt_template)
    chain = LLMChain(llm=llm, prompt=prompt)
    destination_chains[name] = chain

destinations = [f"{p['name']}: {p['description']}" for p in prompt_infos]
destinations_str = "\n".join(destinations)

print(destinations_str)
# default chain ===========================================
default_prompt = ChatPromptTemplate.from_template("{input}")
default_chain = LLMChain(llm=llm, prompt=default_prompt)

# instructions of the task and specific formatting 
MULTI_PROMPT_ROUTER_TEMPLATE = """
Given a raw text input to 
<< FORMATTING >>
return a markdown code snippet with a JSON object formatted
```json
{{{{
    "destination": string \ name of the prompt to use or "Description"
    "next_inputs": string \ a potentially modified version
}}}}
```

REMEMBER: "destination" MUST be one of the candidate prompt
REMEMBER: "next_inputs" can just be the original input if y

<< CANDIDATE PROMPTS >>
{destinations}

<< INPUT >>
{{input}}

<< OUTPUT (remember to include the ```json)>>
"""

# router chain ============================================
router_template = MULTI_PROMPT_ROUTER_TEMPLATE.format(
    destinations=destinations_str
)
router_prompt = PromptTemplate(
    template=router_template,
    input_variables=["input"],
    output_parser=RouterOutputParser(),
)
router_chain = LLMRouterChain.from_llm(llm, router_prompt)

chain = MultiPromptChain(router_chain=router_chain,
                         destination_chains=destination_chains,
                         default_chain=default_chain,
                         verbose=True)
# =========================================================

humamn_inpout = "what is black hole?"
response = chain.run(humamn_inpout)
print(response)