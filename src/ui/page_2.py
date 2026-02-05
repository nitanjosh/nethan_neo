import streamlit as st
import pandas as pd
from data_standardization import convert_date_format, normalize_units, standardize_text_case
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

def app():
    st.title("Data Processing Application")

    df = load_data()

    st.sidebar.header("Data Standardization Options")
    if st.sidebar.button("Standardize Data"):
        df = convert_date_format(df, date_columns=['date_column'], date_format='%Y-%m-%d')
        df = normalize_units(df, unit_mappings={'unit_column': ('old_unit', 'new_unit', 0.001)})
        df = standardize_text_case(df, text_columns=['text_column'], case='lower')
        st.write("### Standardized Data")    
        st.dataframe(df)
        st.sidebar.success("success!")

if __name__ == "__main__":
    app()

