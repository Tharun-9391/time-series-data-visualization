# 📊 Time Series Data Visualization & COVID-19 Prediction Dashboard

This project is a Streamlit-based interactive dashboard that visualizes **COVID-19 prediction results** and allows users to **upload and visualize their own time-series datasets** using various charts. The application supports multiple types of charts and is extendable for general time-series analysis.

---

## 🔧 Features

- 📈 **COVID-19 Case Prediction**: Displays charts for confirmed cases, deaths, and forecasted future cases.
- 📁 **Custom Data Upload**: Users can upload their own time-series `.csv` file and generate visualizations.
- 📊 **Multiple Chart Options**: Line charts, bar graphs, area charts, and more.
- 🧠 **Pre-trained Prediction Model**: Uses a trained time-series model to forecast COVID-19 cases.
- 🖥️ **Streamlit Web App**: Interactive and user-friendly interface.
- 🔄 **Reusable Pipeline**: Works with any univariate time-series data.

---

## 📁 Project Structure

```
time-series-data-visualization/
│
├── covid_model/
│   ├── model.pkl               # Pretrained COVID-19 prediction model
│   └── covid_data.csv          # Historical COVID-19 data
│
├── user_data/
│   └── (Uploaded datasets go here)
│
├── app.py                      # Main Streamlit app
├── utils.py                    # Helper functions
├── requirements.txt            # Required Python packages
└── README.md                   # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/time-series-data-visualization.git
cd time-series-data-visualization
```

### 2. Install Dependencies

Make sure Python 3.7+ is installed. Then run:

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App

```bash
streamlit run app.py
```

---

## 📂 How to Use

### 📌 View COVID-19 Prediction

1. On loading the app, default COVID-19 confirmed, deaths, and prediction charts are shown.
2. The model uses previous data to forecast future trends.

### 📌 Visualize Your Own Time-Series Data

1. Scroll down to the **"Upload Your Dataset"** section.
2. Upload a `.csv` file with:
   - First column: Date or timestamp
   - Second column: Values (e.g., stock price, temperature)
3. Click **Visualize** to generate charts.

---

## 🧪 Model Information

- The model used for COVID-19 prediction is based on a univariate time-series forecasting algorithm (e.g., ARIMA, Prophet, or LSTM).
- Training was done on historical COVID-19 confirmed case data.
- Forecast visualizations help track future trends in pandemic metrics.

---

## ✅ Sample CSV Format

```csv
Date,Value
2020-01-01,100
2020-01-02,105
2020-01-03,110
...
```

---

## 📸 Screenshots

### Dashboard Homepage  
> COVID-19 Visualization + Upload Option  
![dashboard_home](screenshots/home.png)

### Uploaded Data Visualization  
> After user uploads their own dataset  
![uploaded_data](screenshots/uploaded_data.png)

---

## 🛠️ Tools Used

- **Python**
- **Streamlit**
- **Pandas, Numpy**
- **Matplotlib, Plotly, Seaborn**
- **Scikit-learn / Statsmodels**
- **Joblib (for model loading)**

---

## 🙋‍♂️ Author

**Tharun Teja**  
👨‍🎓 Student @ Malla Reddy Engineering College  
💼 Passionate about AI, Data Science & Full-Stack Projects  
📫 [LinkedIn](https://linkedin.com/in/yourprofile) | [GitHub](https://github.com/your-username)

---


## ⭐️ Show Your Support

If you like this project:

- 🌟 Star the repo  
- 🍴 Fork it for customization  
- 🧠 Contribute by reporting issues or creating PRs

---
