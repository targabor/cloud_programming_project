import streamlit as st

looker_report_url = st.secrets["looker_report_url"]

st.markdown(f'<iframe src="{looker_report_url}" width="800" height="600"></iframe>', unsafe_allow_html=True)