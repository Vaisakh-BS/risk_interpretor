import streamlit as st
import requests

st.title("🛡️ Risk Interpreter – SOP Compliance Analyzer")

uploaded_file = st.file_uploader("Upload an SOP PDF", type="pdf")

if uploaded_file is not None:
    with st.spinner("Analyzing..."):
        files = {"file": uploaded_file.getvalue()}
        try:
            response = requests.post("http://localhost:8000/analyze_sop/", files=files)
            if response.status_code == 200:
                st.success("✅ Analysis Complete!")
                result = response.json()["analysis"]
                st.json(result)
            else:
                st.error(f"❌ Error: {response.status_code}")
        except Exception as e:
            st.error(f"⚠️ Failed to connect to backend: {e}")
