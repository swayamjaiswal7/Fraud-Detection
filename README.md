# 🚨 Fraud Detection System (SMOTE + XGBoost + Streamlit Deployment)
## Project Overview

This project focuses on building an end-to-end Fraud Detection Machine Learning system to identify fraudulent financial transactions. Fraud detection is a highly imbalanced classification problem where fraudulent cases occur very rarely compared to legitimate transactions.
To solve this, the project applies advanced preprocessing, feature engineering, imbalance handling (SMOTE), and XGBoost classification, followed by deployment using Streamlit for real-time prediction.

##  Problem Statement
- Financial transaction datasets usually contain a very small fraction of fraud cases, making it difficult for traditional ML models to detect fraud accurately.
The main objective of this project was to:

- Detect fraudulent transactions effectively
-  Handle extreme class imbalance
- Engineer meaningful transaction-based features
- Build a high-performance classification model
- Deploy the trained model as a user-friendly web app using Streamlit

#### Dataset Description
```
The dataset contains transaction records with attributes such as:
Transaction type (TRANSFER / CASH_OUT)
Transaction amount
Sender account balance (before and after)
Receiver account balance (before and after)
Fraud label (isFraud)
Fraudulent transactions mostly occur in TRANSFER and CASH_OUT transaction types, so the dataset was filtered to focus only on these relevant cases.
```
##  Data Preprocessing & Cleaning
```
1️ Transaction Filtering
Only the two transaction types most associated with fraud were used:
TRANSFER
CASH_OUT
This reduced unnecessary noise and improved model focus.

2️ Encoding Transaction Type
The type feature was converted into numerical form:
TRANSFER → 0
CASH_OUT → 1
This ensured the feature could be properly learned by machine learning models.

3️ Handling Balance Anomalies
During exploratory analysis, it was found that many fraud cases contained suspicious balance patterns, such as:
oldbalanceDest = 0
newbalanceDest = 0
transaction amount is non-zero
```
- This anomaly was extremely common in fraudulent cases, but almost absent in non-fraud transactions.

-  Key Insight from Analysis:
```
Nearly ~50% of fraudulent transactions had destination balance anomalies.
Only a negligible fraction of non-fraud transactions showed the same anomaly.

To make this anomaly more meaningful for the model:
destination balances were replaced with -1 for anomaly cases
origin balances were marked as NaN where required
This allowed the model to clearly identify abnormal behavior patterns.
```
##  Feature Engineering
```
To strengthen fraud pattern detection, two additional features were created:
✅ errorbalanceDest
Represents inconsistency in destination balance updates:
oldbalanceDest + amount - newbalanceDest

✅ errorbalanceOrig
Represents inconsistency in origin balance updates:
newbalanceOrig + amount - oldbalanceOrg

Fraudulent transactions often show incorrect or missing balance updates. These engineered features help capture such inconsistencies and improve fraud detection performance.
```
###  Feature Selection
```
Unnecessary columns were removed to avoid noise and reduce dimensionality:
step
nameOrig
nameDest
isFlaggedFraud
These fields do not directly contribute to prediction quality and may introduce bias or leakage.
```
###  Handling Class Imbalance (SMOTE)
```
Why Class Imbalance is a Major Issue?
Fraud detection datasets are heavily imbalanced, meaning:
Legitimate transactions dominate
Fraud cases are extremely rare
If trained normally, a model may simply predict “Not Fraud” always and still achieve high accuracy, but fail in real-world fraud detection.
To solve this issue, SMOTE (Synthetic Minority Oversampling Technique) was applied to generate synthetic fraud samples.
📌 Benefit of SMOTE:
Improves recall for fraud class
Prevents model bias toward majority class
Enhances model learning of fraud patterns
```
### 🤖 Model Building (XGBoost Classifier)
- Why XGBoost?
```
XGBoost is one of the most powerful algorithms for structured/tabular datasets and is widely used in fraud detection problems.
Key advantages:
Handles non-linear relationships effectively
Works well with large-scale datasets
Robust to noisy features
Provides high predictive performance
Supports class imbalance tuning using scale_pos_weight
```

### Model Strategy
```
The model was trained using:
Train-test split
SMOTE oversampling
XGBoost classifier
scale_pos_weight to penalize fraud class misclassification
This ensured the model focuses strongly on minority fraud cases.
```
###  Model Evaluation
```
The model was evaluated using a classification report containing:
Precision
Recall
F1-score
Accuracy
📌 Key Performance Outcome:
Very strong fraud recall (high fraud detection rate)
High precision for fraud class
Overall excellent classification performance
This indicates the model successfully learned fraud transaction patterns despite extreme imbalance.
```

###  Model Deployment 
- After training, the model was saved using joblib as: fraud_xgb_model.pkl
- This makes the model reusable for deployment and production usage.
- The trained fraud detection model was deployed using Streamlit, enabling real-time fraud prediction.
- The Streamlit app provides:
- ✅ Interactive UI for entering transaction details
- ✅ Instant fraud probability prediction
- ✅ Easy-to-use interface for non-technical users
- ✅ Fast inference using saved .pkl model

### 📌 Deployment Workflow
```
The deployment pipeline works as:
User enters transaction inputs (type, balances, amount)
App performs preprocessing & feature engineering
Model loads from fraud_xgb_model.pkl
Prediction is generated using XGBoost
Output is displayed as Fraud / Not Fraud
```
###  Project Structure
```
Fraud-Detection-System/
│
├── app.py                      # Streamlit app script
├── fraud_xgb_model.pkl         # Saved trained XGBoost model
├── requirements.txt            
├── fraud_detection.ipynb
|──README.md                    # Project documentation
└── dataset.csv                
```
###  Key Learnings from the Project
- Fraud detection is not just classification, but a data imbalance + anomaly detection challenge.
- Feature engineering plays a major role in detecting suspicious transaction behavior.
- SMOTE is highly useful for minority class learning.
- XGBoost provides strong performance on structured transaction datasets.
- Streamlit deployment converts an ML model into a real-world usable application.

## ✅ Conclusion

- This project demonstrates an end-to-end fraud detection pipeline, starting from transaction cleaning and anomaly handling to model building using SMOTE + XGBoost, followed by a real-world deployment using Streamlit.
- The final solution is capable of effectively detecting fraudulent transactions in highly imbalanced financial datasets.
