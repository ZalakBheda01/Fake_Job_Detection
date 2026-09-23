import streamlit as st

st.title("📈 Model Performance")
st.caption("Results reported by the supplied machine-learning notebook.")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Accuracy", "97.87%")
c2.metric("Algorithm", "Logistic Regression")
c3.metric("Dataset Size", "17,880")
c4.metric("Fraud Rate", "4.84%")

st.markdown("### Evaluation Metrics")
st.write("The notebook evaluates the model using accuracy, precision, recall, F1-score, classification report, and confusion matrix.")

st.info("The saved-model test in the notebook reports an accuracy of 0.9787 (97.87%).")

st.markdown("### Confusion Matrix")
st.write("The notebook includes a confusion matrix with the classes `Not Fraudulent` and `Fraudulent`. Add the exported matrix image here if you want it displayed directly.")
