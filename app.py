import streamlit as st

st.set_page_config(page_title="Fake Job Detector", page_icon="🕵️", layout="wide")

from console_ui import inject, render, bento, tile, metric, gauge

inject()

TOTAL, FRAUD, LEGIT = 17880, 866, 17014
FRAUD_PCT = FRAUD / TOTAL * 100
LEGIT_PCT = LEGIT / TOTAL * 100

WORKFLOW = [
    "Data Loading", "Data Cleaning", "Missing Value Handling", "Preprocessing",
    "Train/Test Split", "Logistic Regression", "Evaluation", "Prediction",
]

hero = tile(
    '<span class="pill"><i></i>Logistic Regression classifier</span>'
    "<h1>🕵️ Fake Job Detector</h1>"
    '<p class="sub">Machine Learning Dashboard</p>'
    '<p class="lede">Use the sidebar to explore the dataset, model performance, '
    "predictions, and project information.</p>",
    "s8", "hero",
)
rate = tile(
    "<h3>Fraud rate in the dataset</h3>"
    + gauge(FRAUD_PCT, "risk", f"{FRAUD_PCT:.2f}%", f"{FRAUD:,} of {TOTAL:,} postings"),
    "s4",
)

note = tile(
    "<h3>How it works</h3>"
    "<p>This application uses Logistic Regression to classify job postings "
    "as fraudulent or not fraudulent.</p>",
    "s5",
)
steps = "".join(
    f'<div class="step{" last" if i == len(WORKFLOW) - 1 else ""}">'
    f'<div class="n">{i + 1}</div><div class="name">{name}</div></div>'
    for i, name in enumerate(WORKFLOW)
)
flow = tile(f'<h3>Project Workflow</h3><div class="flow">{steps}</div>', "")

render(
    bento(hero, rate),
    bento(
        metric("Dataset Records", f"{TOTAL:,}", "All job postings", "info", "s4", 100),
        metric("Fraudulent Jobs", f"{FRAUD:,}", f"{FRAUD_PCT:.1f}% of records", "risk", "s4", FRAUD_PCT),
        metric("Not Fraudulent", f"{LEGIT:,}", f"{LEGIT_PCT:.1f}% of records", "safe", "s4", LEGIT_PCT),
    ),
    bento(flow),
)
