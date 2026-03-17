#Tenant Churn Prediction using Machine Learning


#Project Overview

This project predicts whether a tenant is likely to churn based on behavioral and property-related data.
It helps property managers identify high-risk tenants and take preventive actions


#Problem Statement

Tenant churn leads to revenue loss and increased costs.
The goal of this project is to build a machine learning model that can predict tenant churn in advance.


#Dataset Description

The dataset contains tenant-related information such as:

Years_in_property

Tenant_age

Rent_amount

Total_rent_paid

avg_session_duration_minutes

number_of_logins_per_month

number_of_support_tickets

satisfaction_score

last_login_days_ago

Target Variable:


#Tenant_churn

0 → Not churn

1 → Churn


#Data Preprocessing

Removed unnecessary columns (e.g., Tenant ID)

Converted categorical variables using one-hot encoding

Ensured all features are numeric

Handled feature mismatch during prediction


#Exploratory Data Analysis (EDA)

More support tickets → Lower satisfaction

Low satisfaction → Higher churn

More logins → Lower churn

Longer session duration → Higher engagement


#Model Building

Algorithm: Random Forest Classifier

Train-Test Split: 80/20

Library: Scikit-learn

#Model Evaluation
#Confusion Matrix:

[[1979 66]
[ 138 817]]


#Performance:

Accuracy: 93.2%

Precision: 92.5%

Recall: 85.5%


#Streamlit Web App

An interactive web application is built using Streamlit.

Features:

User input form

Real-time prediction

Churn probability (%)

Easy-to-use interface


#How to Run the Project
1. Install dependencies

pip install streamlit pandas scikit-learn

2. Run the app

python -m streamlit run app.py

3. Open in browser

http://localhost:8501

#Deployment

You can deploy this project using:

(1)Streamlit Cloud

(2)Render

(3)AWS


#Project Structure

Tenant_Churn_Project/
│
├── app.py
├── Tenant_churn_prediction.csv
├── tenant_churn_model.pkl
├── requirements.txt
└── README.md

#Conclusion

This model successfully predicts tenant churn with high accuracy (~93%).
It helps in identifying at-risk tenants and reducing potential loss.

#Author
Suraj Singh


#Support

If you like this project, give it a ⭐ on GitHub!
