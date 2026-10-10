import streamlit as st

from console_ui import inject, render, bento, tile, chips, page_header

inject()

page_header("ℹ️ About the Project")

render(
    bento(
        tile(
            "<h3>🕵️ Fake Job Detection using Machine Learning</h3>"
            "<p>This project uses machine learning to classify job postings as "
            "<b>fraudulent</b> or <b>not fraudulent</b>.</p>"
        )
    ),
    bento(
        tile(
            "<h3>Dataset</h3><ul>"
            "<li>Total records: <b>17,880</b></li>"
            "<li>Original columns: <b>18</b></li>"
            "<li>Target column: <code>fraudulent</code></li>"
            "<li>Fraudulent records: <b>866</b></li>"
            "<li>Non-fraudulent records: <b>17,014</b></li></ul>",
            "s4",
        ),
        tile("<h3>Machine Learning</h3><p><b>Algorithm:</b> Logistic Regression</p>", "s4"),
        tile(
            "<h3>Model Evaluation</h3><p>The project evaluates the model using:</p><ul>"
            "<li>Accuracy</li><li>Precision</li><li>Recall</li><li>F1-score</li>"
            "<li>Classification report</li><li>Confusion matrix</li></ul>",
            "s4",
        ),
    ),
    bento(
        tile(
            "<h3>Preprocessing</h3><ul>"
            "<li>Salary ranges converted to numerical midpoints</li>"
            "<li>Missing numerical values handled using median</li>"
            "<li>Missing categorical/text values handled using the most frequent value</li>"
            "<li>Categorical features encoded using One-Hot Encoding</li>"
            "<li>Numerical features standardized using StandardScaler</li>"
            "<li><code>job_id</code> and <code>department</code> removed</li></ul>",
            "s8",
        ),
        tile(
            "<h3>Technology</h3>"
            + chips(["Python", "Pandas", "NumPy", "Scikit-learn", "Joblib", "Streamlit"]),
            "s4",
        ),
    ),
)
