import streamlit as st
import pandas as pd

st.title("Dataset Overview")

uploaded_file = st.file_uploader(
    "Upload CSV Dataset",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Preview")

    st.dataframe(df.head())

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", len(df))
    col2.metric("Columns", len(df.columns))
    col3.metric(
        "Missing Values",
        int(df.isnull().sum().sum())
    )

    st.subheader("Column Information")

    st.write(df.dtypes)

else:
    st.info("Upload dataset to continue.")
