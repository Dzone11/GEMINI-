from dotenv import load_dotenv  
load_dotenv()  # load all the env

import streamlit as st
import os
import google.generativeai as genai

# Set the API key directly without using config method
genai.api_key = os.getenv("GOOGLE_API_KEY")

# Function to load gemini pro and get response
model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Initiate streamlit app
st.set_page_config(page_title="Gemini Pro", page_icon=":gem:", layout="wide")
st.title("Gemini LLM Application")

# Text input for user question
input_question = st.text_input("What's up?", key="input")

# Submit button
submit = st.button("Submit")

# When submit is clicked
if submit:
    response = get_gemini_response(input_question)
    st.subheader("Gemini's Response")
    st.write(response)
