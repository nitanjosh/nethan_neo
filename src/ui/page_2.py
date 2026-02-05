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

    st.sidebar.header("Data Standardization Options")

    # Date column selection
    date_columns = st.sidebar.multiselect("Select date columns to standardize (leave as is if not wanted):", options=df.columns)
    #Disable if no date columns are selected
    date_format = st.sidebar.text_input("Enter desired date format (e.g., %Y-%m-%d):", value="%Y-%m-%d", disabled=(len(date_columns) == 0))
    # Unit normalization
    # If no unit normalization is desired, user can leave the fields blank
    unit_column = st.sidebar.selectbox("Select unit column to normalize:", options=df.columns)
    from_unit = st.sidebar.text_input("Enter current unit (e.g., cm):", value="", disabled=(unit_column == ""))
    to_unit = st.sidebar.text_input("Enter desired unit (e.g., m):", value="", disabled=(unit_column == ""))
    factor = st.sidebar.number_input("Enter conversion factor (e.g., 0.01 for cm to m):", value=0.0, disabled=(unit_column == ""))
    # Text case standardization
    text_columns = st.sidebar.multiselect("Select text columns to standardize case:", options=df.columns)
    case_option = st.sidebar.selectbox("Select case option:", options=['lower', 'upper', 'title'], index=0, disabled=(len(text_columns) == 0))

    if st.sidebar.button("Standardize Data"):
        # Apply standardization functions, if the respective options are not blank
        df = convert_date_format(df, date_columns=date_columns, date_format=date_format) if date_columns else df
        df = normalize_units(df, unit_mappings={unit_column: (from_unit, to_unit, factor)}) if unit_column else df
        df = standardize_text_case(df, text_columns=text_columns, case=case_option) if text_columns else df

        st.write("### Standardized Data")    
        st.dataframe(df)
        st.sidebar.success("success!")

if __name__ == "__main__":
    app()

