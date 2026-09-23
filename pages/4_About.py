import streamlit as st

st.title("ℹ️ About the Project")

st.markdown("""
### 🕵️ Fake Job Detection using Machine Learning

This project uses machine learning to classify job postings as **fraudulent** or **not fraudulent**.

### Dataset
- Total records: **17,880**
- Original columns: **18**
- Target column: `fraudulent`
- Fraudulent records: **866**
- Non-fraudulent records: **17,014**

### Machine Learning
**Algorithm:** Logistic Regression

### Preprocessing
- Salary ranges converted to numerical midpoints
- Missing numerical values handled using median
- Missing categorical/text values handled using the most frequent value
- Categorical features encoded using One-Hot Encoding
- Numerical features standardized using StandardScaler
- `job_id` and `department` removed

### Model Evaluation
The project evaluates the model using:
- Accuracy
- Precision
- Recall
- F1-score
- Classification report
- Confusion matrix

### Technology
Python • Pandas • NumPy • Scikit-learn • Joblib • Streamlit
""")
