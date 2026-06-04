import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Task Analysis")

uploaded_file = st.file_uploader(
    "Upload Dataset",
    type=["csv"],
    key="task"
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    task_counts = df["TaskType"].value_counts()

    fig = px.bar(
        x=task_counts.index,
        y=task_counts.values,
        labels={
            "x": "Task Type",
            "y": "Count"
        },
        title="Task Type Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.dataframe(task_counts)

else:
    st.info("Upload dataset.")
