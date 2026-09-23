import streamlit as st
import pandas as pd

st.title("📊 Dashboard")
st.caption("Dataset overview based on the trained notebook.")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Job Postings", "17,880")
c2.metric("Not Fraudulent", "17,014")
c3.metric("Fraudulent", "866")
c4.metric("Fraud Rate", "4.84%")

st.markdown("### Target Distribution")
chart = pd.DataFrame({"Type": ["Not Fraudulent", "Fraudulent"], "Count": [17014, 866]})
st.bar_chart(chart.set_index("Type"))

st.markdown("### Dataset Information")
st.write("The notebook reports 17,880 records and 18 original columns. After removing `job_id` and `department`, 16 columns remain.")
