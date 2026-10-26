from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Initialize Gemini API LLM
llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.5, api_key=os.getenv("GEMINI_API_KEY"))

def generate_response(template, input_variables, inputs):
    prompt = PromptTemplate(template=template, input_variables=input_variables)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(inputs)
