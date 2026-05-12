import streamlit as st
import requests

API_URL = "http://localhost:8000/contracts/analyze"

st.title("AI Contract Review Accelerator")

uploaded_file = st.file_uploader(
    "Upload Contract",
    type=["pdf", "docx"]
)

if uploaded_file:

    files = {
        "file": uploaded_file
    }

    response = requests.post(API_URL, files=files)

    data = response.json()

    st.subheader("Contract Type")
    st.write(data["contract_type"])

    st.subheader("Detected Clauses")
    st.json(data["clauses"])

    st.subheader("Template Deviations")
    st.json(data["deviations"])

    st.subheader("Historical Precedents")
    st.json(data["precedents"])

    st.subheader("AI Review Summary")
    st.write(data["analysis"])

    st.subheader("Routing Decision")
    st.json(data["routing"])

    col1, col2, col3 = st.columns(3)

    with col1:
        st.button("Approve")

    with col2:
        st.button("Escalate")

    with col3:
        st.button("Reject")