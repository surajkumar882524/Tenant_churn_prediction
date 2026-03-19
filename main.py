import pandas as pd
import joblib
import pickle

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, OrdinalEncoder
from sklearn.ensemble import RandomForestClassifier

# =========================
# Load Data
# =========================
df = pd.read_csv("Tenant_churn_prediction.csv")

# Drop unnecessary columns
df.drop(columns=['Tenant_id','signup_date'], inplace=True)

# feature selection based on EDA insights
features=['Years_in_property','income_level','subscription_type','Rent_amount','Total_rent_paid','usage_frequency','avg_session_duration_minutes','number_of_logins_per_month','number_of_support_tickets',
         'satisfaction_score','Lease_type','last_login_days_ago','promotional_response','discount_used','Tenant_churn']
df_ml=df[features]

# Target
target = "Tenant_churn"

X = df_ml.drop(columns=[target])
y = df_ml[target]

# =========================
# Column Groups
# =========================

# Binary categorical (from your notebook)
binary_cols = ['Lease_type','promotional_response','discount_used']

# Multi-category
multi_cat_cols = ['income_level','subscription_type','usage_frequency']

# Numeric columns
num_cols = [col for col in X.columns if col not in binary_cols + multi_cat_cols]

# =========================
# Preprocessing
# =========================

preprocessor = ColumnTransformer([
    
    # Binary → Ordinal (0/1)
    ("binary", OrdinalEncoder(
        handle_unknown='use_encoded_value', 
        unknown_value=-1
    ), binary_cols),
    
    # Multi-category → OneHot
    ("onehot", OneHotEncoder(
        handle_unknown='ignore'
    ), multi_cat_cols),
    
    # Numeric → Scaling
    ("num", MinMaxScaler(), num_cols)
])

# =========================
# Pipeline
# =========================

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", RandomForestClassifier(
        n_estimators=200,
        max_depth=10,
        random_state=42
    ))
])

# =========================
# Train-Test Split
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================
# Train Model
# =========================

pipeline.fit(X_train, y_train)

# =========================
# Save Files
# =========================

# Full pipeline (BEST)
joblib.dump(pipeline, "pipeline.joblib")

# Only model
pickle.dump(pipeline.named_steps['model'], open("model.pkl", "wb"))

print("Pipeline trained & saved successfully!")