import streamlit as st
import requests

st.title("🏠 House Price Prediction App")

sqft = st.number_input("Square Feet (sqft_living)", min_value=100)
bedrooms = st.number_input("Bedrooms", min_value=1)
bathrooms = st.number_input("Bathrooms", min_value=1)

if st.button("Predict Price"):

    url = "https://house-prediction-2xix.onrender.com/api/predict"

    data = {
        "sqft_living": sqft,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms
    }


    try:
        response = requests.post(url, json=data, timeout=30)

        # Agar status code 200 nahi hai to error throw kare
        response.raise_for_status()
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Price: ${result['predicted_price']}")
        else:
            st.error(f"Api Error: {response.status_code} -  {response.text}")

    except requests.exceptions.ConnectionError:
        st.error("❌ Cannot connect to API. Make sure FastAPI server is running.")

    try:
        response=requests.post(url, json=data, timeout=5)
        response.raise_for_status()
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Price: ${result['predicted_price']}")
        else:
            st.error(f"Api Error: {response.status_code} - {response.text0}")
    except requests.exceptions.ConnectionError:
        st.error(" Cannot connect to api. Make sure Fastapi Server is running.")

