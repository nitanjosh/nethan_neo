import streamlit as st
from ui.page_1 import app as page_1_app

st.set_page_config(page_title="Data Processing Application", layout="wide")
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Data Cleaning"])

if page == "Data Cleaning":
    page_1_app()

