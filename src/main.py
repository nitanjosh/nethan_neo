import streamlit as st
from ui.page_1 import app as page_1_app
from ui.page_2 import app as page_2_app

st.set_page_config(page_title="Data Processing Application", layout="wide")
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Data Cleaning", "Data Standardization"])

if page == "Data Cleaning":
    page_1_app()
elif page == "Data Standardization":
    page_2_app()
