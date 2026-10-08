import streamlit as st
import pandas as pd
import joblib
from datetime import date

st.set_page_config(
    page_title="Hostel Food Requirement Prediction",
    layout="centered"
)

model = joblib.load("food_requirement_adaboost.pkl")

st.title("Hostel Food Requirement Prediction")

st.write(
    "Predict the number of meals required in a hostel based on the number of students and other factors."
)

selected_date = st.date_input(
    "Date",
    value=date.today(),
)

meal_type = st.selectbox(
    "Meal Type",
    options=["Breakfast", "Lunch", "Dinner"]
)

hostel_occupancy = st.number_input(
    "Number of Residents",
    min_value=1,
    max_value=5000,
    value=500,
    step=1
)

weather = st.selectbox(
    "Weather",
    options=["Sunny", "Rainy", "Cloudy"]
)

temperature = st.number_input(
    "Temperature (°C)",
    min_value=-0,
    max_value=50,
    value=30,
    step=1
)

exam_period = st.selectbox(
    "Exam Period",
    options=["Yes", "No"]
)

festival = st.selectbox(
    "Festival / Holiday",
    options=["Yes", "No"]
)

weekend = st.selectbox(
    "Weekend",
    options=["Yes", "No"]
)

buffer_percentage = st.slider(
    "Safety Buffer (%)",
    min_value=0,
    max_value=15,
    value=5,
    step=1
)
day_of_week = selected_date.strftime("%A")

month = selected_date.month

day_of_month = selected_date.day

input_data = pd.DataFrame({
    "Day_of_Week": [day_of_week],
    "Meal_Type": [meal_type],
    "Hostel_Occupancy": [hostel_occupancy],
    "Weather": [weather],
    "Temperature": [temperature],
    "Exam_Period": [exam_period],
    "Festival": [festival],
    "Weekend": [weekend],
    "Month": [month],
    "Day_of_Month": [day_of_month]
})

if st.button("Predict Food Requirement"):
    prediction = model.predict(input_data)[0]

    prediction = max(0, round(prediction))

    recommended_meals = round(
        prediction * (1 + buffer_percentage / 100)
    )

    st.subheader("Prediction")

    st.success(
        f"Expected consumption: **{prediction} meals**"
    )

    st.info(
        f"Recommended meals to prepare: **{recommended_meals} meals**"
    )

    st.write(
        f"Safety buffer: **{buffer_percentage}%**"
    )