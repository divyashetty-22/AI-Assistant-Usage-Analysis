import streamlit as st

st.set_page_config(
    page_title="AI Assistant Usage Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Assistant Usage Dashboard")

st.markdown("""
### Welcome

This dashboard analyzes how students use AI Assistants.

Use the pages in the sidebar to explore:

- Dataset Overview
- Task Analysis
- Satisfaction Analysis
""")

st.success("Select a page from the sidebar.")
