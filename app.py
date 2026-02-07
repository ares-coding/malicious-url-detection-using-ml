import streamlit as st
import numpy as np

st.set_page_config(
    page_title="Malicious URL Detection",
    layout="centered"
)

st.title("🔐 Malicious URL Detection System")
st.caption("Machine Learning-based URL Classification")

url = st.text_input(
    "Enter URL to scan",
    placeholder="https://example.com"
)

if st.button("Scan URL"):
    # --- MOCK FEATURES 
    features = {
        "URL Length": len(url),
        "Special Characters": sum(not c.isalnum() for c in url),
        "HTTPS Used": url.startswith("https"),
        "Domain Age": "New"
    }

    prediction = "MALICIOUS"
    confidence = 0.92

    st.divider()

    if prediction == "MALICIOUS":
        st.error("⚠️ Status: MALICIOUS")
    else:
        st.success("✅ Status: SAFE")

    st.metric("Confidence Score", f"{confidence * 100:.1f}%")

    st.subheader("Extracted Features")
    st.json(features)
