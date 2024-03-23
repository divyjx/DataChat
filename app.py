import streamlit as st 
import pandas as pd

st.header('Welcome to DataChat App')
file = st.file_uploader("Upload your csv file", type='csv')
if file:
    data = pd.read_csv(file)
    data.to_csv("data/data.csv", index=0)
    

chat_type = st.radio('Base Model', ['ChatGPT (openai)', 'Gemini (google)'])
api_key = st.text_input("Enter API key")
