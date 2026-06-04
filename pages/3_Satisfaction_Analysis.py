import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Satisfaction Analysis")

uploaded_file = st.file_uploader(
    "Upload Dataset",
    type=["csv"],
    key="satisfaction"
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    satisfaction = (
        df.groupby("TaskType")["SatisfactionRating"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        satisfaction,
        x="TaskType",
        y="SatisfactionRating",
        title="Average Satisfaction by Task"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.dataframe(satisfaction)

else:
    st.info("Upload dataset.")
