REQUIRED_COLUMNS = [
    "age",
    "income",
    "balance",
    "transactions"
]

def validate_columns(df):

    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]

    if missing_cols:
        return False, missing_cols

    return True, None




import joblib

model = joblib.load("model.pkl")

def make_predictions(df):

    preds = model.predict(df)

    df["prediction"] = preds

    return df


import streamlit as st
import pandas as pd

from utils.validator import validate_columns
from utils.predictor import make_predictions

st.title("ML Prediction App")

st.write("Upload a CSV file to generate predictions.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Data")
    st.dataframe(df.head())

    # Validate Columns
    valid, missing = validate_columns(df)

    if not valid:

        st.error(f"Missing required columns: {missing}")

    else:

        st.success("All required columns present")

        if st.button("Run Prediction"):

            results = make_predictions(df)

            st.subheader("Prediction Results")

            st.dataframe(results)

            csv = results.to_csv(index=False)

            st.download_button(
                label="Download Predictions",
                data=csv,
                file_name="predictions.csv",
                mime="text/csv"
            )