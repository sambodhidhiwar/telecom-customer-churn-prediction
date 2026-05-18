# 🚀 Telecom Customer Churn Prediction System
<img width="1911" height="906" alt="image" src="https://github.com/user-attachments/assets/84ea4bde-42ca-4ba2-b276-c027a220bbaa" />

# 🌐 Website of Deployed AI Application

🚀 Click below to use the deployed AI application:

[Telecom Customer Churn Prediction App](https://telecom-churn-prediction-by-sambodhi-dhiwar.streamlit.app/)

## 📌 Project Overview

The **Telecom Customer Churn Prediction System** is a Machine Learning based web application developed to predict whether a telecom customer is likely to leave (churn) or stay with the company.

This project uses **Logistic Regression Classification** along with a modern **Streamlit Dashboard UI** to provide real-time churn prediction and customer risk analysis.

The main objective of this project is to help telecom companies identify high-risk customers early and improve customer retention strategies.

---

# 🎯 Problem Statement

Customer churn is one of the major challenges faced by telecom companies. Losing customers directly impacts company revenue and growth.

This project aims to:

- Analyze customer behavior
- Identify churn patterns
- Predict customer churn probability
- Help businesses take preventive actions

---

# 🧠 Machine Learning Model Used

## Logistic Regression

The project uses **Logistic Regression**, a supervised machine learning classification algorithm.

### Why Logistic Regression?

- Efficient for binary classification
- Fast training and prediction
- Interpretable results
- Good performance on structured datasets

The model predicts:

0 → Customer Will Stay  
1 → Customer Will Churn

---

# 📂 Dataset Information

Dataset used:

**Telco Customer Churn Dataset**

The dataset contains customer-related telecom information such as:

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Internet Service
- Tech Support
- Streaming Services
- Contract Type
- Payment Method
- Monthly Charges
- Total Charges

---

# 🔍 Exploratory Data Analysis (EDA)

Several EDA techniques were performed to understand the dataset.

## ✔ Data Cleaning

- Handled missing values
- Converted categorical columns into numerical values
- Removed unnecessary columns
- Converted data types properly

---

## ✔ Data Visualization

Visualizations were created using:

- Matplotlib
- Seaborn

Charts included:

- Customer churn distribution
- Correlation analysis
- Service-based churn analysis
- Contract type analysis
- Payment method analysis

---

# ⚙ Feature Engineering

Categorical variables were encoded using Label Encoding.

Features and target variables were separated into:

- X → Input Features
- y → Target Variable (Churn)

---

# 🧪 Model Training

The dataset was split using Train-Test Split.

Training and testing data were created for proper model evaluation.

The Logistic Regression model was then trained successfully on the telecom dataset.

---

# 📈 Model Evaluation

The model was evaluated using multiple performance metrics.

## ✔ Accuracy Score

Accuracy Achieved: **~82%**

This indicates strong predictive capability for telecom churn classification.

---

## ✔ Confusion Matrix

A confusion matrix was generated to analyze:

- True Positives
- True Negatives
- False Positives
- False Negatives

This helped evaluate prediction quality in detail.

---

## ✔ Classification Report

The project also evaluated:

- Precision
- Recall
- F1-Score
- Support

These metrics provided deeper insight into model performance.

---

# 💾 Model Saving

The trained model was saved using Joblib.

Saved model file:

`churn_model.pkl`

This allows the trained model to be reused without retraining.

---

# 🌐 Streamlit Web Application

A fully interactive Streamlit web application was developed for deployment.

## Features of the Dashboard

### ✅ Modern Neon Purple UI

- Glassmorphism cards
- Dark futuristic theme
- Responsive layout
- Professional dashboard design

---

### ✅ Customer Input Filters

Users can provide customer details through:

- Dropdown menus
- Sliders
- Numeric inputs

---

### ✅ Real-Time Prediction

The dashboard predicts whether:

- Customer Will Stay
- Customer Will Churn

---

### ✅ Churn Probability

The application calculates churn probability and displays:

- Churn percentage
- Animated progress bar

---

### ✅ Customer Risk Analysis

The dashboard classifies customers into:

- LOW RISK
- MEDIUM RISK
- HIGH RISK

based on churn probability.

---

### ✅ Interactive Charts

Charts were added to visualize:

- Customer metrics
- Churn analysis
- Feature comparison

---

# 🛠 Technologies Used

## Programming Language

- Python

---

## Libraries Used

### Data Processing

- Pandas
- NumPy

### Visualization

- Matplotlib
- Seaborn

### Machine Learning

- Scikit-learn

### Model Saving

- Joblib

### Deployment

- Streamlit

---

# 📁 Project Structure

```text
├── app.py
├── churn_model.pkl
├── requirements.txt
├── Telco-Customer-Churn.csv
└── Telecom Customer Churn Prediction.ipynb
```

---

# 🚀 Deployment

The project is deployed using:

- GitHub
- Streamlit Community Cloud

This makes the application accessible publicly through a live web link.

---

# 📊 Future Improvements

Possible future enhancements:

- XGBoost / Random Forest models
- Better feature engineering
- Real telecom API integration
- Database connectivity
- Authentication system
- Advanced analytics dashboard
- Real-time customer monitoring

---

# 🏁 Conclusion

The Telecom Customer Churn Prediction System successfully demonstrates the practical implementation of Machine Learning in solving real-world business problems.

The project combines:

- Data Analysis
- Machine Learning
- Data Visualization
- Web Deployment
- UI/UX Design

to build a complete end-to-end AI-powered predictive analytics solution.

This project can help telecom companies improve customer retention strategies and reduce revenue loss due to customer churn.

---

# 👨‍💻 Developed By

## Sambodhi Dhiwar
