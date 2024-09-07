from dotenv import load_dotenv

load_dotenv() # Load environmental variables from .env 

import streamlit as st 
import os 
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialise Gemini Pro model 
model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text

def read_image(uploaded_file):
    if uploaded_file is not None:
        data = uploaded_file.getvalue()

        image_parts = [
            {
                'mime_type': uploaded_file.type,
                'data': data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("no file uploaded")
    

# Initialise Streamlit App

st.set_page_config(page_title= "Gemini Pro Demo")

st.header("Multi Language Invoice Extractor")
input = st.text_input ("Input Prompt: ", key="input")
uploaded_file= st.file_uploader("Upload the Invoice...", type=["jpg", "jpeg", "png", "pdf"])

image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Invoice", use_column_width=True)  # Display upladed image 

submit = st.button("Tell me about the invoice")

input_prompt = """
You are an accountant. You will answer questions based on the uploaded invoices

"""

if submit:
    image_data = read_image(uploaded_file)
    response=get_gemini_response(input_prompt, image_data, input)
    st.subheader("The response is ")
    st.write(response)

