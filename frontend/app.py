import streamlit as st
import requests
import pandas as pd

# -----------------------------
# Backend API URL
# -----------------------------
BACKEND_URL = "http://127.0.0.1:8000/predict"

# -----------------------------
# App title
# -----------------------------
st.set_page_config(page_title="Used Car Price Predictor", page_icon="🚗")
st.title("🚗 Used Car Price Predictor")

# -----------------------------
# Input fields
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    Year = st.number_input("Year", min_value=1995, max_value=2024, value=2016)
    Kilometers_Driven = st.number_input("Kilometers Driven", min_value=0, max_value=300000, value=50000)
    Seats = st.number_input("Seats", min_value=2, max_value=10, value=5)

    Mileage = st.number_input("Mileage (km/l)", min_value=5.0, max_value=40.0, value=18.0)
    Engine = st.number_input("Engine (CC)", min_value=600, max_value=5000, value=1200)
    Power = st.number_input("Power (bhp)", min_value=40.0, max_value=500.0, value=80.0)

with col2:
    Location = st.selectbox("Location", ["mumbai", "delhi", "bangalore", "chennai", "kolkata"])
    Fuel_Type = st.selectbox("Fuel Type", ["petrol", "diesel", "cng", "lpg"])
    Transmission = st.selectbox("Transmission", ["manual", "automatic"])
    Owner_Type = st.selectbox("Owner Type", ["first", "second", "third"])
    Brand = st.selectbox("Brand", ["maruti", "hyundai", "honda", "toyota"])
    Model = st.text_input("Model", value="unknown")

# -----------------------------
# Predict button
# -----------------------------
if st.button("Predict Price 💰"):
    payload = {
        "Location": Location,
        "Year": Year,
        "Kilometers_Driven": Kilometers_Driven,
        "Fuel_Type": Fuel_Type,
        "Transmission": Transmission,
        "Owner_Type": Owner_Type,
        "Seats": Seats,
        "Brand": Brand,
        "Model": Model,
        "Mileage_KMPH": Mileage,
        "Engine_CC": Engine,
        "Power_BHP": Power
    }

    try:
        response = requests.post(BACKEND_URL, json=payload)

        if response.status_code == 200:
            price = response.json()["predicted_price"]
            st.success(f"💰 Estimated Price: ₹ {price:.2f} Lakhs")
        else:
            st.error(f"❌ Backend error: {response.status_code}")
            st.json(response.json())

    except requests.exceptions.ConnectionError:
        st.error("❌ Cannot connect to backend. Is FastAPI running?")
    except Exception as e:
        st.error(f"❌ Unexpected error: {e}")
