import streamlit as st
import joblib
import numpy as np
import pandas as pd

# ===================================
# PAGE CONFIG
# ===================================

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="🚀",
    layout="wide"
)

# ===================================
# LOAD MODEL
# ===================================

model = joblib.load("churn_model.pkl")

# ===================================
# CUSTOM CSS
# ===================================

st.markdown("""
<style>

/* BACKGROUND */

.stApp {
    background: linear-gradient(135deg,#050816,#0b1026,#120c2e);
}

/* REMOVE TOP SPACE */

header {
    visibility: hidden;
}

.main .block-container {
    padding-top: 1rem;
    padding-left: 1rem;
    padding-right: 1rem;
}

/* SIDEBAR */

[data-testid="stSidebar"] {
    background: rgba(10,10,35,0.98);
    border-right: 1px solid rgba(255,255,255,0.06);
}

/* SIDEBAR TITLE */

.sidebar-title {
    font-size: 42px;
    font-weight: 800;
    color: #d946ef;
    line-height: 1.1;
}

.sidebar-subtitle {
    color: #a855f7;
    font-size: 16px;
    margin-bottom: 35px;
}

/* MAIN TITLE */

.main-title {
    font-size: 60px;
    font-weight: 800;
    color: white;
    margin-bottom: 5px;
}

.main-subtitle {
    color: #c084fc;
    font-size: 22px;
    margin-bottom: 25px;
}

/* CARDS */

.custom-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 24px;
    padding: 30px;
    box-shadow: 0px 0px 30px rgba(168,85,247,0.12);
}

/* METRICS */

.metric-title {
    color: #d8b4fe;
    font-size: 20px;
    margin-bottom: 15px;
}

.metric-value {
    font-size: 72px;
    font-weight: 800;
    color: white;
}

/* LABELS */

label {
    color: #f5d0fe !important;
    font-weight: 600 !important;
}

/* DROPDOWNS */

.stSelectbox div[data-baseweb="select"] {
    background-color: white !important;
    border-radius: 14px !important;
    border: 1px solid rgba(168,85,247,0.3);
}

.stSelectbox div[data-baseweb="select"] * {
    color: black !important;
}

/* NUMBER INPUT */

.stNumberInput input {
    background-color: white !important;
    color: black !important;
    border-radius: 14px !important;
    border: 1px solid rgba(168,85,247,0.3);
}

/* SLIDER LINE */

.stSlider [data-baseweb="slider"] > div > div {
    background-color: #2a2a40 !important;
}

/* SLIDER DOT */

.stSlider [role="slider"] {
    background-color: #a855f7 !important;
    border: 3px solid #d8b4fe !important;
}

/* BUTTON */

.stButton>button {
    background: linear-gradient(90deg,#9333ea,#c026d3);
    color: white;
    border: none;
    border-radius: 18px;
    width: 100%;
    height: 65px;
    font-size: 24px;
    font-weight: 700;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.01);
    box-shadow: 0px 0px 20px #9333ea;
}

</style>
""", unsafe_allow_html=True)

# ===================================
# SIDEBAR
# ===================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">📊 Customer<br>Churn</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-subtitle">Prediction System</div>',
        unsafe_allow_html=True
    )

    st.markdown("## Customer Filters")

    gender = st.selectbox(
        "Gender",
        [0,1],
        format_func=lambda x:
        "Female" if x == 0 else "Male"
    )

    seniorcitizen = st.selectbox(
        "Senior Citizen",
        [0,1],
        format_func=lambda x:
        "No" if x == 0 else "Yes"
    )

    partner = st.selectbox(
        "Partner",
        [0,1],
        format_func=lambda x:
        "No" if x == 0 else "Yes"
    )

    dependents = st.selectbox(
        "Dependents",
        [0,1],
        format_func=lambda x:
        "No" if x == 0 else "Yes"
    )

    tenure = st.slider(
        "Tenure (Months)",
        0,72,12
    )

    phoneservice = st.selectbox(
        "Phone Service",
        [0,1],
        format_func=lambda x:
        "No" if x == 0 else "Yes"
    )

    multiplelines = st.selectbox(
        "Multiple Lines",
        [0,1,2],
        format_func=lambda x:
        "No" if x == 0 else
        "Yes" if x == 1 else
        "No Phone Service"
    )

    internetservice = st.selectbox(
        "Internet Service",
        [0,1,2],
        format_func=lambda x:
        "DSL" if x == 0 else
        "Fiber Optic" if x == 1 else
        "No Internet Service"
    )

    onlinesecurity = st.selectbox(
        "Online Security",
        [0,1,2],
        format_func=lambda x:
        "No" if x == 0 else
        "Yes" if x == 1 else
        "No Internet Service"
    )

    onlinebackup = st.selectbox(
        "Online Backup",
        [0,1,2],
        format_func=lambda x:
        "No" if x == 0 else
        "Yes" if x == 1 else
        "No Internet Service"
    )

    deviceprotection = st.selectbox(
        "Device Protection",
        [0,1,2],
        format_func=lambda x:
        "No" if x == 0 else
        "Yes" if x == 1 else
        "No Internet Service"
    )

    techsupport = st.selectbox(
        "Tech Support",
        [0,1,2],
        format_func=lambda x:
        "No" if x == 0 else
        "Yes" if x == 1 else
        "No Internet Service"
    )

    streamingtv = st.selectbox(
        "Streaming TV",
        [0,1,2],
        format_func=lambda x:
        "No" if x == 0 else
        "Yes" if x == 1 else
        "No Internet Service"
    )

    streamingmovies = st.selectbox(
        "Streaming Movies",
        [0,1,2],
        format_func=lambda x:
        "No" if x == 0 else
        "Yes" if x == 1 else
        "No Internet Service"
    )

    contract = st.selectbox(
        "Contract Type",
        [0,1,2],
        format_func=lambda x:
        "Month-to-Month" if x == 0 else
        "One Year" if x == 1 else
        "Two Year"
    )

    paperlessbilling = st.selectbox(
        "Paperless Billing",
        [0,1],
        format_func=lambda x:
        "No" if x == 0 else "Yes"
    )

    paymentmethod = st.selectbox(
        "Payment Method",
        [0,1,2,3],
        format_func=lambda x:
        "Electronic Check" if x == 0 else
        "Mailed Check" if x == 1 else
        "Bank Transfer" if x == 2 else
        "Credit Card"
    )

    monthlycharges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        max_value=150.0,
        value=70.0
    )

# ===================================
# AUTO TOTAL CHARGES
# ===================================

totalcharges = monthlycharges * tenure

# ===================================
# MAIN TITLE
# ===================================

st.markdown(
    '<div class="main-title">🚀 Telecom Customer Churn Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-subtitle">AI Powered Customer Retention Analysis Dashboard</div>',
    unsafe_allow_html=True
)

# ===================================
# TOP CARDS
# ===================================

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
    <div class="custom-card">
        <div class="metric-title">Prediction Overview</div>
        <div class="metric-value">82%</div>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="custom-card">
        <div class="metric-title">Model Accuracy</div>
        <div class="metric-value">0.82</div>
    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown(f"""
    <div class="custom-card">
        <div class="metric-title">Estimated Total Charges</div>
        <div class="metric-value" style="font-size:40px;">
        ₹ {round(totalcharges,2)}
        </div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ===================================
# CENTER BUTTON
# ===================================

btn1, btn2, btn3 = st.columns([1,2,1])

with btn2:
    predict_button = st.button("🔮 Predict Churn")

# ===================================
# PREDICTION
# ===================================

if predict_button:

    input_data = pd.DataFrame({

        "gender":[gender],
        "SeniorCitizen":[seniorcitizen],
        "Partner":[partner],
        "Dependents":[dependents],
        "tenure":[tenure],
        "PhoneService":[phoneservice],
        "MultipleLines":[multiplelines],
        "InternetService":[internetservice],
        "OnlineSecurity":[onlinesecurity],
        "OnlineBackup":[onlinebackup],
        "DeviceProtection":[deviceprotection],
        "TechSupport":[techsupport],
        "StreamingTV":[streamingtv],
        "StreamingMovies":[streamingmovies],
        "Contract":[contract],
        "PaperlessBilling":[paperlessbilling],
        "PaymentMethod":[paymentmethod],
        "MonthlyCharges":[monthlycharges],
        "TotalCharges":[totalcharges]

    })

    prediction = model.predict(input_data)

    probability = model.predict_proba(input_data)[0][1]

    percentage = round(probability * 100, 2)

    st.write("")

    # RESULT CARDS

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(f"""
        <div class="custom-card">
            <div class="metric-title">Churn Probability</div>
            <div class="metric-value">{percentage}%</div>
        </div>
        """, unsafe_allow_html=True)

        st.progress(int(percentage))

    with col2:

        if percentage < 30:

            risk = "LOW RISK"
            color = "#22c55e"

        elif percentage < 70:

            risk = "MEDIUM RISK"
            color = "#facc15"

        else:

            risk = "HIGH RISK"
            color = "#ef4444"

        st.markdown(f"""
        <div class="custom-card">
            <div class="metric-title">Customer Risk Level</div>
            <div style="
                font-size:50px;
                font-weight:800;
                color:{color};
            ">
                {risk}
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # FINAL RESULT

    if prediction[0] == 1:

        st.error("⚠️ Customer is likely to churn")

    else:

        st.success("✅ Customer is likely to stay")

    st.write("")

    # CHARTS

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:

        st.markdown("### 📈 Customer Metrics")

        chart_data = {
            "Feature": [
                "Tenure",
                "Monthly Charges",
                "Total Charges"
            ],
            "Value": [
                tenure,
                monthlycharges,
                totalcharges
            ]
        }

        st.bar_chart(chart_data, x="Feature", y="Value")

    with chart_col2:

        st.markdown("### 📊 Churn Analysis")

        pie_data = {
            "Category": ["Stay", "Churn"],
            "Value": [100 - percentage, percentage]
        }

        st.bar_chart(pie_data, x="Category", y="Value")

st.markdown("---")
st.markdown("###  Developed by Sambodhi Dhiwar ")
