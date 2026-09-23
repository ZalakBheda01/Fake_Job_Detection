import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.title("🔍 Predict Job")
st.write("Enter the job-posting details and use the saved Logistic Regression pipeline.")

model_path = Path(__file__).parents[1] / "model" / "fake_job_detection_logistic_regression.pkl"

if not model_path.exists():
    st.warning("Model file not found. Put `fake_job_detection_logistic_regression.pkl` inside the `model` folder.")
    st.stop()

model = joblib.load(model_path)

def salary_to_midpoint(value):
    if not value.strip():
        return None
    try:
        low, high = map(float, value.replace(",", "").split("-"))
        return (low + high) / 2
    except:
        return None

with st.form("prediction_form"):
    c1, c2 = st.columns(2)
    with c1:
        title = st.text_input("Job Title *")
        location = st.text_input("Location")
        salary_range = st.text_input("Salary Range", placeholder="e.g. 40000-60000")
        employment_type = st.selectbox("Employment Type", ["Not Available", "Full-time", "Part-time", "Contract", "Temporary", "Other"])
        required_experience = st.selectbox("Required Experience", ["Not Available", "Internship", "Entry level", "Associate", "Mid-Senior level", "Director", "Executive"])
        required_education = st.selectbox("Required Education", ["Not Available", "High School or equivalent", "Associate Degree", "Bachelor's Degree", "Master's Degree", "Doctorate", "Professional"])
    with c2:
        industry = st.text_input("Industry")
        function = st.text_input("Function")
        telecommuting = st.selectbox("Telecommuting", [0, 1], format_func=lambda x: "Yes" if x else "No")
        has_company_logo = st.selectbox("Has Company Logo", [0, 1], format_func=lambda x: "Yes" if x else "No")
        has_questions = st.selectbox("Has Questions", [0, 1], format_func=lambda x: "Yes" if x else "No")

    company_profile = st.text_area("Company Profile")
    description = st.text_area("Description *")
    requirements = st.text_area("Requirements")
    benefits = st.text_area("Benefits")

    submitted = st.form_submit_button("🔍 Check Job Posting", use_container_width=True)

if submitted:
    data = pd.DataFrame([{
        "title": title,
        "location": location,
        "salary_range": salary_to_midpoint(salary_range),
        "company_profile": company_profile,
        "description": description,
        "requirements": requirements,
        "benefits": benefits,
        "telecommuting": telecommuting,
        "has_company_logo": has_company_logo,
        "has_questions": has_questions,
        "employment_type": employment_type,
        "required_experience": required_experience,
        "required_education": required_education,
        "industry": industry,
        "function": function
    }])
    try:
        pred = int(model.predict(data)[0])
        if pred == 1:
            st.error("⚠️ Potentially Fraudulent Job")
        else:
            st.success("✅ Not Classified as Fraudulent")

        if hasattr(model, "predict_proba"):
            probability = model.predict_proba(data)[0][pred]
            st.metric("Model Confidence", f"{probability * 100:.2f}%")
    except Exception as e:
        st.error(f"Prediction error: {e}")
