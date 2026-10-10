import streamlit as st

from console_ui import inject, render, bento, tile, metric, gauge, hbar, page_header

inject()

TOTAL, LEGIT, FRAUD = 17880, 17014, 866
FRAUD_PCT = FRAUD / TOTAL * 100
BAR_MAX = max(LEGIT, FRAUD)

page_header("📊 Dashboard", "Dataset overview based on the trained notebook.")

render(
    bento(
        metric("Total Job Postings", f"{TOTAL:,}", tone="info", pct=100),
        metric("Not Fraudulent", f"{LEGIT:,}", tone="safe", pct=LEGIT / TOTAL * 100),
        metric("Fraudulent", f"{FRAUD:,}", tone="risk", pct=FRAUD_PCT),
        metric("Fraud Rate", f"{FRAUD_PCT:.2f}%", tone="risk", pct=FRAUD_PCT),
    ),
    bento(
        tile("<h3>Target Distribution</h3>" + gauge(FRAUD_PCT, "risk", f"{FRAUD_PCT:.2f}%", "of postings are fraudulent"), "s5"),
        tile(
            "<h3>Count by Type</h3>"
            + hbar("Not Fraudulent", f"{LEGIT:,}", LEGIT / BAR_MAX * 100, "safe")
            + hbar("Fraudulent", f"{FRAUD:,}", FRAUD / BAR_MAX * 100, "risk"),
            "s7",
        ),
    ),
    bento(
        tile(
            "<h3>Dataset Information</h3>"
            '<div class="mini">'
            "<div><b>18</b><span>original columns</span></div>"
            "<div><b>2</b><span>removed: <code>job_id</code>, <code>department</code></span></div>"
            "<div><b>16</b><span>columns remain</span></div>"
            "</div>"
            f"<p>The notebook reports {TOTAL:,} records and 18 original columns. "
            "After removing <code>job_id</code> and <code>department</code>, 16 columns remain.</p>",
        )
    ),
)
