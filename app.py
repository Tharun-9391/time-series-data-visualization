# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import BayesianRidge, LinearRegression
from datetime import timedelta
from utils import preprocess_data

st.set_page_config(layout="wide", page_title="Time Series Dashboard")

st.title("📊 Time Series Visualization & Prediction Dashboard")
st.markdown("This dashboard shows COVID-19 analytics and allows you to visualize any time-series dataset by uploading your own CSV.")

# --- Section 1: Show your own COVID-19 data ---
st.header("📌 Project Output: COVID-19 Dataset")

df = pd.read_csv("static/sample_dataset.csv")
df = preprocess_data(df)

# Rename if needed
if "Confirmed Cases" in df.columns:
    df.rename(columns={"Confirmed Cases": "Confirmed"}, inplace=True)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Confirmed Cases")
    if "Confirmed" in df.columns:
        st.line_chart(df.set_index('Date')["Confirmed"])
    else:
        st.warning("Column 'Confirmed' not found.")

with col2:
    st.subheader("Deaths")
    if "Deaths" in df.columns:
        st.line_chart(df.set_index('Date')["Deaths"])
    else:
        st.warning("Column 'Deaths' not found.")

# --- Future Prediction ---
st.subheader("🔮 Future Prediction (Bayesian Ridge vs Linear Regression)")
if "Confirmed" in df.columns:
    df["Days"] = (df["Date"] - df["Date"].min()).dt.days
    X = df[["Days"]]
    y = df["Confirmed"]

    # Train both models
    bayesian_model = BayesianRidge()
    linear_model = LinearRegression()
    bayesian_model.fit(X, y)
    linear_model.fit(X, y)

    # Future prediction setup
    future_days = 30
    start_date = df["Date"].min()
    last_date = df["Date"].max()
    future_dates = [last_date + timedelta(days=i) for i in range(1, future_days + 1)]
    future_day_vals = [(d - start_date).days for d in future_dates]
    X_future = pd.DataFrame({"Days": future_day_vals})

    # Predict
    bayesian_preds = bayesian_model.predict(X_future)
    linear_preds = linear_model.predict(X_future)

    # Combine predictions
    future_df = pd.DataFrame({
        "Date": future_dates,
        "Bayesian Ridge": bayesian_preds,
        "Linear Regression": linear_preds
    }).set_index("Date")

    st.line_chart(future_df)
else:
    st.warning("Confirmed column not found. Cannot generate prediction.")

# --- Section 2: User Data Upload & Visualization ---
st.header("📥 Visualize Your Own Time-Series Data")

uploaded_file = st.file_uploader("Upload your CSV file (must contain a date column)", type=["csv"])
if uploaded_file:
    user_df = pd.read_csv(uploaded_file)

    try:
        user_df = preprocess_data(user_df)
        st.success("✅ Data uploaded and processed successfully!")
        st.dataframe(user_df.head())

        feature_cols = [col for col in user_df.columns if col != "Date"]
        selected_features = st.multiselect("Select columns to visualize", feature_cols)

        chart_type = st.selectbox("Select Chart Type", ["Line", "Bar", "Area"])

        if st.button("📈 Visualize"):
            for col in selected_features:
                st.subheader(f"{chart_type} Chart for {col}")
                if chart_type == "Line":
                    st.line_chart(user_df.set_index("Date")[col])
                elif chart_type == "Bar":
                    st.bar_chart(user_df.set_index("Date")[col])
                elif chart_type == "Area":
                    fig, ax = plt.subplots()
                    ax.fill_between(user_df["Date"], user_df[col], alpha=0.3)
                    ax.plot(user_df["Date"], user_df[col])
                    ax.set_title(col)
                    st.pyplot(fig)

    except Exception as e:
        st.error(f"❌ Failed to process data: {e}")
else:
    st.info("Upload a CSV file with a date column to start visualizing.")
