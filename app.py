# # =========================
# # app.py (Streamlit - Improved)
# # =========================
# import streamlit as st
# import pandas as pd
# import joblib

# st.set_page_config(page_title="Tenant Churn Prediction", layout="wide")

# st.title("Tenant Churn Prediction App")
# st.write("Upload a CSV or Excel file to predict tenant churn.")

# # Load trained pipeline
# @st.cache_resource
# def load_pipeline():
#     return joblib.load("pipeline.joblib")

# pipeline = load_pipeline()

# # File upload
# uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

# if uploaded_file is not None:
#     try:
#         # Read file
#         if uploaded_file.name.endswith(".csv"):
#             data = pd.read_csv(uploaded_file)
#         else:
#             data = pd.read_excel(uploaded_file)

#         st.subheader(" Data Preview")
#         st.dataframe(data.head())

#         # Predict button
#         if st.button(" Predict"):
#             predictions = pipeline.predict(data)

#             # Add predictions
#             data["Prediction"] = predictions

#             st.subheader("Predictions")
#             st.dataframe(data)

#             # Download results
#             csv = data.to_csv(index=False).encode("utf-8")
#             st.download_button(
#                 label="⬇ Download Predictions",
#                 data=csv,
#                 file_name="predictions.csv",
#                 mime="text/csv"
#             )

#     except Exception as e:
#         st.error(" Error occurred while processing file")
#         st.code(str(e))

# # =========================
# # requirements.txt
# # =========================
# # =========================
# # pandas
# # scikit-learn
# # streamlit
# # joblib


# =========================
# app.py (Streamlit - Batch + Single Prediction)
# =========================
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Tenant Churn Prediction", layout="wide")
# =========================
# Background Image + Overlay
# =========================
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1560518883-ce09059eeffa");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

[data-testid="stAppViewContainer"]::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.6); /* dark overlay */
    z-index: 0;
}

[data-testid="stHeader"], [data-testid="stToolbar"] {
    background: rgba(0,0,0,0);
}

.main {
    position: relative;
    z-index: 1;
    color: white;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)


st.title("🏠 Tenant Churn Prediction App")
# =========================
# App Description
# =========================
st.markdown("""
### 📌 About this App
This app predicts whether a tenant is likely to **churn (leave)** or **stay** using a trained Machine Learning model.

---

### ⚙️ Features Used in Model (with Description)
Your uploaded file **must contain ALL these columns exactly**:

- **Years_in_property** → Number of years tenant has stayed in the property  
- **income_level** → Tenant income category *(low / medium / high)*  
- **subscription_type** → Type of subscription plan *(basic / standard / premium)*  
- **Rent_amount** → Monthly rent amount paid by tenant  
- **Total_rent_paid** → Total rent paid over time  
- **usage_frequency** → How often tenant uses the service *(low / medium / high)*  
- **avg_session_duration_minutes** → Average time spent per session  
- **number_of_logins_per_month** → Number of times tenant logs in monthly  
- **number_of_support_tickets** → Issues raised by tenant  
- **satisfaction_score** → Satisfaction rating *(1–10)*  
- **Lease_type** → Lease duration *(monthly / yearly)*  
- **last_login_days_ago** → Days since last activity  
- **promotional_response** → Responded to promotions *(yes / no)*  
- **discount_used** → Whether discounts were used *(yes / no)*  

---

""")




# Load trained pipeline
@st.cache_resource
def load_pipeline():
    return joblib.load("pipeline.joblib")

pipeline = load_pipeline()

# =========================
# Sidebar Mode Selection
# =========================
mode = st.sidebar.radio("Choose Mode", ["Batch Prediction (Upload File)", "Single Prediction (Manual Input)"])

# =========================
# 1. Batch Prediction
# =========================
if mode == "Batch Prediction (Upload File)":
    st.header("📂 Upload File for Batch Prediction")

    uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith(".csv"):
                data = pd.read_csv(uploaded_file)
            else:
                data = pd.read_excel(uploaded_file)

            st.subheader("📊 Data Preview")
            st.dataframe(data.head())

            if st.button("🔍 Predict (Batch)"):
                predictions = pipeline.predict(data)
                data["Prediction"] = predictions

                st.subheader("✅ Predictions")
                st.dataframe(data)

                csv = data.to_csv(index=False).encode("utf-8")
                st.download_button(
                    label="⬇ Download Predictions",
                    data=csv,
                    file_name="predictions.csv",
                    mime="text/csv"
                )

        except Exception as e:
            st.error("⚠️ Error occurred while processing file")
            st.code(str(e))

# =========================
# 2. Single Prediction
# =========================
else:
    st.header("🧾 Enter Details for Single Prediction")

    # Layout
    col1, col2 = st.columns(2)

    with col1:
        Years_in_property = st.number_input("Years in Property", min_value=0)
        income_level = st.selectbox("Income Level", ["low", "medium", "high"])
        subscription_type = st.selectbox("Subscription Type", ["basic", "standard", "premium"])
        Rent_amount = st.number_input("Rent Amount")
        Total_rent_paid = st.number_input("Total Rent Paid")
        usage_frequency = st.selectbox("Usage Frequency", ["low", "medium", "high"])
        avg_session_duration_minutes = st.number_input("Avg Session Duration (minutes)")

    with col2:
        number_of_logins_per_month = st.number_input("Logins per Month", min_value=0)
        number_of_support_tickets = st.number_input("Support Tickets", min_value=0)
        satisfaction_score = st.number_input("Satisfaction Score", min_value=1, max_value=10)
        Lease_type = st.selectbox("Lease Type", ["monthly", "yearly"])
        last_login_days_ago = st.number_input("Last Login Days Ago", min_value=0)
        promotional_response = st.selectbox("Promotional Response", ["yes", "no"])
        discount_used = st.selectbox("Discount Used", ["yes", "no"])

    if st.button("🔮 Predict (Single)"):
        input_data = pd.DataFrame([{
            "Years_in_property": Years_in_property,
            "income_level": income_level,
            "subscription_type": subscription_type,
            "Rent_amount": Rent_amount,
            "Total_rent_paid": Total_rent_paid,
            "usage_frequency": usage_frequency,
            "avg_session_duration_minutes": avg_session_duration_minutes,
            "number_of_logins_per_month": number_of_logins_per_month,
            "number_of_support_tickets": number_of_support_tickets,
            "satisfaction_score": satisfaction_score,
            "Lease_type": Lease_type,
            "last_login_days_ago": last_login_days_ago,
            "promotional_response": promotional_response,
            "discount_used": discount_used
        }])

        try:
            prediction = pipeline.predict(input_data)[0]

            st.subheader("🎯 Prediction Result")

            if prediction == 0:
                st.error("⚠️ High Risk: Tenant likely to leave")
            else:
                st.success("✅ Low Risk: Tenant likely to stay")

        except Exception as e:
            st.error(" Error in prediction")
            st.code(str(e))

# =========================
# requirements.txt
# =========================
# =========================
# =========================
# pandas
# scikit-learn
# streamlit
# joblib
