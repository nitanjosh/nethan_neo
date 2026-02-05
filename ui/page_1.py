import streamlit as st
import pandas as pd
from src.data_cleaning import replace_with_none, trim_whitespace, remove_duplicates
from src.config import DATA_DIRECTORY

@st.cache_data
def load_data():
    return pd.read_csv(DATA_DIRECTORY)

def app():
    st.title("Data Processing Application")

    df = load_data()

    st.sidebar.header("Data Cleaning Options")
    if st.sidebar.button("Clean Data"):
        df = replace_with_none(df)
        df = trim_whitespace(df)
        df = remove_duplicates(df)
        st.write("### Cleaned Data")    
        st.dataframe(df)
        st.sidebar.success("success!")
    else:
        st.sidebar.feedback("Data did not process.")

if __name__ == "__main__":
    app()

