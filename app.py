import streamlit as st

st.set_page_config(page_title="Fake Job Detector", page_icon="🕵️", layout="wide")

st.title("🕵️ Fake Job Detector")
st.subheader("Machine Learning Dashboard")
st.write("Use the sidebar to explore the dataset, model performance, predictions, and project information.")

st.info("This application uses Logistic Regression to classify job postings as fraudulent or not fraudulent.")

c1, c2, c3 = st.columns(3)
c1.metric("Dataset Records", "17,880")
c2.metric("Fraudulent Jobs", "866")
c3.metric("Not Fraudulent", "17,014")

st.markdown("---")
st.markdown("### Project Workflow")
st.write("Data Loading → Data Cleaning → Missing Value Handling → Preprocessing → Train/Test Split → Logistic Regression → Evaluation → Prediction")
