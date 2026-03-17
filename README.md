# TENANT CHURN PREDICTION USING MACHINE LEARNING



## PROJECT OVERVIEW

This project predicts whether a tenant is likely to churn based on behavioral and property-related data.
It helps property managers identify high-risk tenants and take preventive actions
#




## PROBLEM STATEMENT

Tenant churn leads to revenue loss and increased costs.
The goal of this project is to build a machine learning model that can predict tenant churn in advance.

#


## DATASET DESCRIPTION

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
#



## TENANT_CHURN

0 → Not churn

1 → Churn
#




## DATA PREPROCESSING

(1) Removed unnecessary columns (e.g., Tenant ID)

(2) Converted categorical variables using one-hot encoding

(3) Ensured all features are numeric

(4) Handled feature mismatch during prediction
#





## EXPLORARTRY DATA  ANALYSIS (EDA)

(1) More support tickets → Lower satisfaction

(2) Low satisfaction → Higher churn

(3) More logins → Lower churn

(4) Longer session duration → Higher engagement
#





## MODEL BUILDING

(1) Algorithm: Random Forest Classifier

(2) Train-Test Split: 80/20

(3) Library: Scikit-learn
#





## MODEL EVALUATION

Confusion Matrix

[[1979 66]

[ 138 817]]
#





## PERFORMANCE

(1) Accuracy: 93.2%

(2) Precision: 92.5%

(3) Recall: 85.5%
#





## STREAMLIT WEB APP

An interactive web application is built using Streamlit.

Features:

(1) User input form

(2) Real-time prediction

(3) Churn probability (%)

(4) Easy-to-use interface
#





## HOW TO RUN THE PROJECT
1. Install dependencies

pip install streamlit pandas scikit-learn

2. Run the app

python -m streamlit run app.py

3. Open in browser

http://localhost:8501
#





## DEPLOYMENT

You can deploy this project using:

(1) Streamlit Cloud

(2) Render

(3) AWS
#





## PROJECT STRUCTURE

Tenant_Churn_Project/

│

├── app.py

├── Tenant_churn_prediction.csv

├── tenant_churn_model.pkl

├── requirements.txt

└── README.md
#





## CONCLUSION

This model successfully predicts tenant churn with high accuracy (~93%).
It helps in identifying at-risk tenants and reducing potential loss.
#




## AUTHOR

Suraj Singh
#



## SUPPORT

If you like this project, give it a ⭐ on GitHub!
