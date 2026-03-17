import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.title("🏠 Tenant Churn Prediction App")
st.write("Predict whether a tenant will churn based on behavior and property data.")

uploaded_file = st.file_uploader("Upload Tenant Dataset CSV", type=["csv"])

if uploaded_file:

    data = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.write(data.head())

    # ---------------------------
    # DATA CLEANING
    # ---------------------------

    data = data.drop(columns=["Tenant_id","signup_date"], errors="ignore")

    data = pd.get_dummies(data, drop_first=True)

    X = data.drop("Tenant_churn", axis=1)
    y = data["Tenant_churn"]

    # Train model
    model = RandomForestClassifier(random_state=42)
    model.fit(X, y)

    st.success("Model trained successfully!")

    feature_columns = X.columns

    # ---------------------------
    # USER INPUT SECTION
    # ---------------------------

    st.subheader("Enter Tenant Details")

    with st.form("prediction_form"):

        Years_in_property = st.number_input("Years in Property", 0, 20)
        Tenant_age = st.number_input("Tenant Age", 18, 80)
        Rent_amount = st.number_input("Rent Amount")
        Total_rent_paid = st.number_input("Total Rent Paid")
        avg_session_duration_minutes = st.number_input("Avg Session Duration (minutes)")
        number_of_logins_per_month = st.number_input("Logins per Month")
        number_of_support_tickets = st.number_input("Support Tickets")
        satisfaction_score = st.slider("Satisfaction Score", 1, 10)
        last_login_days_ago = st.number_input("Last Login Days Ago")

        submit_button = st.form_submit_button("Predict Churn")

    if submit_button:

        # Create empty dataframe with training columns
        input_data = pd.DataFrame(columns=feature_columns)
        input_data.loc[0] = 0

        # Fill only numeric columns
        input_data["Years_in_property"] = Years_in_property
        input_data["Tenant_age"] = Tenant_age
        input_data["Rent_amount"] = Rent_amount
        input_data["Total_rent_paid"] = Total_rent_paid
        input_data["avg_session_duration_minutes"] = avg_session_duration_minutes
        input_data["number_of_logins_per_month"] = number_of_logins_per_month
        input_data["number_of_support_tickets"] = number_of_support_tickets
        input_data["satisfaction_score"] = satisfaction_score
        input_data["last_login_days_ago"] = last_login_days_ago

        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.error("⚠️ Tenant is likely to CHURN")
        else:
            st.success("✅ Tenant is NOT likely to churn")