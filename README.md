
## Fraud Detection Streamlit App
A machine learning web application built with Streamlit to detect fraudulent financial transactions. The app uses a Logistic Regression model trained on transaction features such as amount, sender balance, and receiver balance to predict whether a transaction is fraudulent (1) or legitimate (0).
### 📌 Features

- Interactive Streamlit UI for user input.

- Predicts if a transaction is likely to be fraudulent.

- Displays fraud probability and binary classification result.

- Reproducible ML pipeline with scikit-learn.

### Clone Repo
git clone https://github.com/swayamjaiswal7/Fraud-Detection.git
cd Fraud-Detection

### Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate # Mac/Linux

### Install Dependencies
pip install -r requirements.txt

### Run App
streamlit run index.py

### Usage
 ##### Enter Transaction Details
 - Amount
 - Old Balance (Sender)
 - New Balance (Sender)
 - Old Balance (Receiver)
 - New Balance (Receiver)
 - Type
 
 ##### Click Predict
 
 ### App will display whether the Transaction is Fraud or Not

 # Model Used
 
 - Logistic Regression
 - Imbalanced Class Handling (SMOTE)

 ## Deployed on streamlit

 ## Demo Screenshot
 <img width="786" height="860" alt="image" src="https://github.com/user-attachments/assets/163a5ef7-02c0-4313-bfaa-bd1394608a53" />


