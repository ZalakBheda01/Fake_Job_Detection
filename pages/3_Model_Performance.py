import streamlit as st
from pathlib import Path

from console_ui import inject, render, bento, tile, metric, gauge, chips, page_header

inject()

ACCURACY = 97.87

page_header("📈 Model Performance", "Results reported by the supplied machine-learning notebook.")

render(
    bento(
        metric("Accuracy", f"{ACCURACY:.2f}%", tone="safe", pct=ACCURACY),
        metric("Algorithm", "Logistic Regression", tone="info", small=True),
        metric("Dataset Size", "17,880"),
        metric("Fraud Rate", "4.84%", tone="risk", pct=4.84),
    ),
    bento(
        tile(
            "<h3>Evaluation Metrics</h3>"
            "<p>The notebook evaluates the model using accuracy, precision, recall, F1-score, "
            "classification report, and confusion matrix.</p>"
            + '<div style="margin-top:1rem">'
            + chips(["Accuracy", "Precision", "Recall", "F1-score", "Classification report", "Confusion matrix"])
            + "</div>",
            "s7",
        ),
        tile(
            "<h3>Saved-model accuracy</h3>"
            + gauge(ACCURACY, "safe", f"{ACCURACY:.2f}%", "accuracy 0.9787 on the notebook test"),
            "s5",
        ),
    ),
    bento(
        tile(
            "<h3>Confusion Matrix</h3>"
            "<p>The notebook includes a confusion matrix with the classes <code>Not Fraudulent</code> "
            "and <code>Fraudulent</code>. Add the exported matrix image here if you want it displayed directly.</p>"
        )
    ),
)

# Optional: save the exported image as assets/confusion_matrix.png and it appears here.
image_path = Path(__file__).parents[1] / "assets" / "confusion_matrix.png"
if image_path.exists():
    st.image(str(image_path), use_container_width=True)
