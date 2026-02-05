import streamlit as st
from ui.page_1 import app as page_1_app
from data_cleaning import replace_with_none, trim_whitespace, remove_duplicates

st.set_page_config(page_title="Data Processing Application", layout="wide")
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Data Cleaning"])

if page == "Data Cleaning":
    page_1_app()

