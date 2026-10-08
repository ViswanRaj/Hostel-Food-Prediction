# 🍛 Hostel Food Requirement Predictor

## 📌 Project Overview
A machine learning application that predicts the expected number of meals required in a hostel/mess based on factors such as day of the week, meal type, hostel occupancy, weather, temperature, exam periods, festivals, and weekends.

The goal is to help hostel/mess kitchens reduce food waste and avoid food shortages.

## 🤖 Machine Learning Model
- Algorithm: AdaBoost Regressor
- Base Estimator: Decision Tree Regressor
- Preprocessing: One-Hot Encoding
- Target: Actual Consumption

## 📊 Features Used
- Day of Week
- Meal Type
- Hostel Occupancy
- Weather
- Temperature
- Exam Period
- Festival
- Weekend
- Month
- Day of Month

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

## 📁 Project Structure

Food-Waste-Predictor/
│
├── app.py
├── food_requirement_adaboost.pkl
├── requirements.txt
├── README.md
└── dataset/
    └── hostel_food_waste_dataset.csv

## 🚀 How to Run

### 1. Create virtual environment

```bash
python -m venv .venv