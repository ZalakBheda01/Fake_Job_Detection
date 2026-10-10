import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

from console_ui import inject, render, bento, tile, gauge, chips, page_header

inject()

page_header("🔍 Predict Job", "Enter the job-posting details and use the saved Logistic Regression pipeline.")

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
    except ValueError:
        return None


def posting_gaps(salary_range, company_profile, requirements, description, has_company_logo, has_questions):
    """Plain observations about the entered details. These are not the model's reasons."""
    gaps = []
    if not has_company_logo:
        gaps.append("No company logo")
    if not has_questions:
        gaps.append("No screening questions")
    if not salary_range.strip():
        gaps.append("No salary listed")
    elif salary_to_midpoint(salary_range) is None:
        gaps.append("Salary not in low-high format")
    if not company_profile.strip():
        gaps.append("Company profile is empty")
    if not requirements.strip():
        gaps.append("Requirements are empty")
    if len(description.strip()) < 200:
        gaps.append("Short description (under 200 characters)")
    return gaps


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
    if not title.strip() or not description.strip():
        st.warning("Job Title and Description are required. Fill both in and check again.")
        st.stop()

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
        "function": function,
    }])
    try:
        pred = int(model.predict(data)[0])
        fraud = pred == 1
        tone = "risk" if fraud else "safe"
        headline = "Potentially Fraudulent Job" if fraud else "Not Classified as Fraudulent"

        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(data)[0]
            fraud_pct = float(proba[1]) * 100
            confidence = float(proba[pred]) * 100
        else:
            fraud_pct = 100.0 if fraud else 0.0
            confidence = None

        conf_html = f"<div><b>{confidence:.2f}%</b><span>Model confidence</span></div>" if confidence is not None else ""
        gaps = posting_gaps(salary_range, company_profile, requirements, description, has_company_logo, has_questions)
        gaps_html = chips(gaps, "risk") if gaps else chips(["No obvious gaps in the details you entered"], "safe")

        render(
            bento(
                tile(
                    "<h3>Fraud risk</h3>" + gauge(fraud_pct, tone, f"{fraud_pct:.1f}%", "probability the posting is fraudulent"),
                    "s5",
                ),
                tile(
                    f"<h2>{headline}</h2>"
                    f'<div class="stats"><div><b>{fraud_pct:.2f}%</b><span>Fraud probability</span></div>{conf_html}</div>'
                    "<h4>Details worth double-checking</h4>"
                    f"{gaps_html}"
                    '<p class="fine">These notes describe what you entered. They are not the model\'s reasons for its verdict.</p>',
                    "s7", f"verdict {tone}",
                ),
            )
        )
    except Exception as e:
        st.error(f"Prediction error: {e}")
