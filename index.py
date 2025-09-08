import streamlit as st
import pandas as pd
import joblib

# Load trained model

model = joblib.load(r"fraud_detection.pkl")

# Define all expected columns (must match training time)
ALL_COLUMNS = [
    "amount",
    "oldbalanceOrg",
    "newbalanceOrig",
    "oldbalanceDest",
    "newbalanceDest",
    "type_CASH_IN",
    "type_CASH_OUT",
    "type_DEBIT",
    "type_PAYMENT",
    "type_TRANSFER"
]

st.title("💳 Fraud Detection App")
st.write("Enter transaction details below to predict if it's fraudulent:")

# User inputs
amount = st.number_input("Transaction Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=5000.0)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=4000.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=2000.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=3000.0)

txn_type = st.selectbox(
    "Transaction Type",
    ["CASH_IN", "CASH_OUT", "DEBIT", "PAYMENT", "TRANSFER"]
)

if st.button("Predict Fraud"):
    # Create input dataframe with all expected columns
    input_data = pd.DataFrame(columns=ALL_COLUMNS)
    input_data.loc[0] = 0  # initialize with zeros

    # Fill numeric values
    input_data.at[0, "amount"] = float(amount)
    input_data.at[0, "oldbalanceOrg"] = float(oldbalanceOrg)
    input_data.at[0, "newbalanceOrig"] = float(newbalanceOrig)
    input_data.at[0, "oldbalanceDest"] = float(oldbalanceDest)
    input_data.at[0, "newbalanceDest"] = float(newbalanceDest)

    # One-hot encode transaction type
    col_name = f"type_{txn_type}"
    if col_name in input_data.columns:
        input_data.at[0, col_name] = 1

    # Prediction
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    # Show results
    if prediction == 1:
        st.error(f"⚠️ Fraudulent Transaction Detected! (Probability: {probability:.2f})")
    else:
        st.success(f"✅ Legitimate Transaction (Fraud Probability: {probability:.2f})")


