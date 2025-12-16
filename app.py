# Importing Dependencies
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Implementing LangSmith Configuration
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_PROJECT'] = 'Q&A ChatBot'

# Defining Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', 'You are a helpful assistant. Please respond to the users question concisely.'),
        ('user', 'Question : {question}')
    ]
)

# Function to generate response from the model
def generate_response(question, api_key, llm, temperature, max_tokens):
    model = ChatGroq(model = llm, api_key = api_key, temperature = temperature, max_tokens = max_tokens)
    output_parser = StrOutputParser()
    chain = prompt|model|output_parser
    answer = chain.invoke({'question' : question})
    return answer

# Streamlit App Interface
st.title('Q&A ChatBot')

st.sidebar.title('Settings')
api_key = st.sidebar.text_input('Enter your Groq API Key', type = 'password')
llm = st.sidebar.selectbox('Select Language Model', ['llama-3.3-70b-versatile', 'llama-3.1-8b-instant', 'qwen/qwen3-32b'])
temperature = st.sidebar.slider('Temperature', min_value = 0.0, max_value = 1.0, value = 0.7)
max_tokens = st.sidebar.slider('Max Tokens', min_value = 50, max_value = 300, value = 150)

st.write('Ask any question and get a concise answer!')
user_input = st.text_input('Your Question : ')
if user_input and api_key:
    response = generate_response(user_input, api_key, llm, temperature, max_tokens)
    st.write(response)
elif user_input and not api_key:
    st.write('Please enter your Groq API Key in the sidebar to get a response.')
else:
    st.write('Please enter a question to get started.')
