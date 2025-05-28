import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("pta_rules_of_origin.csv")

st.title("📘 PTA Rules of Origin Explorer")

# Search box
query = st.text_input("Search for keyword:")
if query:
    result = df[df['Text'].str.contains(query, case=False)]
    st.write(f"Results for '{query}': {len(result)} rows found")
    st.dataframe(result)
else:
    st.dataframe(df)

# Filter by Article
article = st.selectbox("Filter by Article:", ["All"] + list(df['Article'].unique()))
if article != "All":
    st.dataframe(df[df['Article'] == article])