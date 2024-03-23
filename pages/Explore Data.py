import streamlit as st 
import pandas as pd 
import os 

def analyse_values(df:pd.DataFrame):
    columns = df.columns
    st.write(columns)
    values = dict.fromkeys(columns)
    for col in columns:
        values[col] = df[col].value_counts()
    
    st.write(values)

data_files = os.listdir('data')
if (len(data_files)==0): 
    exit(0)

df_file = st.radio('Pick a uploaded file',data_files)
if df_file:
    df = pd.read_csv(f'data/{df_file}')
    st.dataframe(df)

    choices = ['per columns valeus analysis']
    action = st.radio('Choose an action to perform on the file', choices)
    
    if (action == choices[0]):
        analyse_values(df)