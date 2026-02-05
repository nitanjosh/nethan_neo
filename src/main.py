import streamlit as st
import pandas as pd
import numpy as np




st.title("Annual Compounding Interest Calculator")

col1, col2, col3= st.columns(3)
amount = col1.number_input("Enter Amount:")
interest = col2.number_input("Enter Interest Rate:", min_value=0.01)
year = col3.number_input("Enter Number of Years:", min_value=1)
year = int(year)

#Amount Computed
interest_per_year = interest/100
final_amount = amount * (1+interest_per_year)**year
interest_accum = final_amount - amount

col1, col2, col3 = st.columns(3)

#Display Metrics
initial = col1.metric(label="### Initial Amount:", value=f"${amount:,.2f}")
int_amt = col2.metric(label="### Interest Accumulated:", value=f"${interest_accum:,.2f}")
fin_amt = col3.metric(label="### Interest Amount", value=f"${final_amount:,.2f}")

#Create Data Frame
data = []
current_amount = amount

for i in range(1, year + 1):
    current_amount *= (1 + interest_per_year)
    data.append([i, current_amount])

df = pd.DataFrame(data, columns=["Year", "Amount"])

#Output Dataframe
st.write("### Compounding Interest Graph")
st.line_chart(df.set_index("Year"))