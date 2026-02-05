import streamlit as st
import pandas as pd
import numpy as np
from data_cleaning import replace_with_none, trim_whitespace, remove_duplicates

DATA_DIRECTORY = "https://raw.githubusercontent.com/nitanjosh/nethan_neo/main/dataset/Test_File.csv"

df = pd.read_csv(DATA_DIRECTORY)
#input null for null values in dataframe

st.title("Data Cleaning Application")

st.sidebar.header("Data Cleaning Options")
if st.sidebar.button("Clean Data"):
    df = replace_with_none(df)
    df = trim_whitespace(df)
    df = remove_duplicates(df)
    st.write("### Cleaned Data")
    st.dataframe(df)
    st.sidebar.success("success!")


