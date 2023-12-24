from dotenv import load_dotenv  
load_dotenv()  # load all the env

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Set the API key directly without using config method
genai.api_key = os.getenv("GOOGLE_API_KEY")

# Function to load gemini pro and get response
model = genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input_text, image):
    if input_text != "":
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content(image)
    return response.text

# Initiate streamlit app
st.set_page_config(page_title="Gemini Pro Vision", page_icon=":gem:", layout="wide")

st.header("Gemini Vision Pro App")
input_text = st.text_input("How may I assist you today?", key="input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
submit = st.button("How do you feel about this image?")

# If submit is clicked
if submit:
    response = get_gemini_response(input_text, image)
    st.subheader("Gemini's Response")
    st.write(response)
