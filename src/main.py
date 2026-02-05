import streamlit as st
import pandas as pd
import numpy as np

DATA_DIRECTORY = "https://raw.githubusercontent.com/nitanjosh/nethan_neo/main/dataset/Test_File.csv"

st.title("Sample Dataset")

df = pd.read_csv(DATA_DIRECTORY)

#input null for null values in dataframe
df = df.replace({np.nan: None})


st.dataframe(df)

st.write("Statistical Summary:")
st.write(df.describe())


