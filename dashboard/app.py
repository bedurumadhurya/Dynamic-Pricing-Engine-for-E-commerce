import streamlit as st
import requests
import datetime

st.title("🛍️ Dynamic Pricing Dashboard")

# Input fields
timestamp = st.datetime_input("Timestamp", datetime.datetime.now())
product_id = st.number_input("Product ID", 101)
demand = st.number_input("Demand", 20)
inventory = st.number_input("Inventory", 50)
season = st.selectbox("Season", ["summer", "winter", "spring", "autumn"])
day_of_week = st.number_input("Day of Week (1=Mon)", 1)
hour = st.number_input("Hour", 10)

if st.button("Get Price"):
    # ✅ Define features before using them
    features = {
        "timestamp": str(timestamp),
        "product_id": product_id,
        "demand": demand,
        "inventory": inventory,
        "season": season,
        "day_of_week": day_of_week,
        "hour": hour
    }

    try:
        response = requests.post("http://127.0.0.1:5000/predict", json=features)
        result = response.json()

        if response.status_code == 200:
            if "predicted_optimal_price" in result:
                st.success(f"💰 Recommended Price: ₹{result['predicted_optimal_price']}")
            else:
                st.error(f"Backend error: {result.get('error', 'Unknown error')}")
        else:
            st.error(f"Prediction failed. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"Connection error: {e}")

