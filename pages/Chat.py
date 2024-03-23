import streamlit as st 
import pandas as pd 
import os 


if 'data.csv' in os.listdir('data'):
    st.write(
        "A data file has been found. If you intent to use other data file then upload new file in app section."
    )
    df = pd.read_csv('data/data.csv')
    # st.write(df.describe())

    