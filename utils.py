# utils.py
import pandas as pd

def preprocess_data(df):
    date_cols = [col for col in df.columns if 'date' in col.lower()]
    if not date_cols:
        raise ValueError("No column found with 'date' in its name.")
    date_col = date_cols[0]

    df[date_col] = pd.to_datetime(df[date_col], dayfirst=True, errors='coerce')
    df = df.dropna(subset=[date_col])
    df = df.sort_values(by=date_col).reset_index(drop=True)
    df.rename(columns={date_col: "Date"}, inplace=True)
    return df

# Optional: your model functions
# utils.py
from sklearn.linear_model import BayesianRidge
import numpy as np

def train_bayesian_model(df, target_col):
    df = df.dropna(subset=[target_col])
    df["Days"] = (df["Date"] - df["Date"].min()).dt.days
    X = df[["Days"]]
    y = df[target_col]

    model = BayesianRidge()
    model.fit(X, y)

    # Save the model and metadata to return
    df.attrs["model"] = model
    df.attrs["start_date"] = df["Date"].min()
    df.attrs["last_date"] = df["Date"].max()


from datetime import timedelta

def predict_future(df, days_ahead=30):
    import numpy as np
    model = df.attrs.get("model")
    start_date = df.attrs.get("start_date")
    last_date = df.attrs.get("last_date")

    if model is None or start_date is None or last_date is None:
        return pd.DataFrame()

    future_dates = [last_date + timedelta(days=i) for i in range(1, days_ahead + 1)]
    future_days = [(d - start_date).days for d in future_dates]
    predictions = model.predict(np.array(future_days).reshape(-1, 1))

    future_df = pd.DataFrame({
        "Date": future_dates,
        "Predicted": predictions
    })

    return future_df

