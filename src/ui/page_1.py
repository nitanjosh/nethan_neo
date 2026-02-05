import streamlit as st
import pandas as pd
from data_cleaning import replace_with_none, trim_whitespace, remove_duplicates
from config import DATA_DIRECTORY

def app():
    st.title("Data Processing Application")

    upload_dataset = st.file_uploader("Upload your CSV file:", type=["csv"])

    if upload_dataset is None:
        st.info("Upload your dataset to continue")
        return

    df = pd.read_csv(upload_dataset)
    raw_data = df.copy()
    data_to_process = df.copy()

    st.subheader("Original Data")
    st.dataframe(raw_data)

    st.sidebar.header("Data Cleaning Options")

    if st.sidebar.button("Clean Data"):
        df = replace_with_none(data_to_process)
        df = trim_whitespace(df)
        df = remove_duplicates(df)

        st.subheader("Cleaned Data")
        st.dataframe(df)
        st.sidebar.success("success!")

if __name__ == "__main__":
    app()
