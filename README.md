# 🏠 House Price Prediction System

## 📌 Project Overview

This project is a **House Price Prediction System** built using Machine Learning.
It predicts house prices based on various features such as location, area, number of rooms, etc.

The project consists of:

* Backend API built with FastAPI
* Frontend UI built using Streamlit
* Machine Learning model for prediction

---

## 🚀 Tech Stack

* Python
* FastAPI (Backend API)
* Streamlit (Frontend UI)
* Scikit-learn (ML Model)
* Pandas & NumPy (Data Processing)

---

## ⚙️ Features

* Predict house prices using trained ML model
* User-friendly UI with Streamlit
* REST API for prediction
* Handles missing/null values in dataset
* Scalable backend using FastAPI

---

## 🧠 Machine Learning

* Model: Linear Regression
* Dataset: House price dataset (kc_house_data.csv)
* Data preprocessing:

  * Handling null values
  * Feature selection
  * Data normalization

## ▶️ How to Run Project

### 1️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 2️⃣ Run FastAPI server

```
uvicorn main:app --reload
```

### 3️⃣ Run Streamlit app

```
streamlit run app.py
```

---

## 🔗 API Endpoint

* POST /predict
  👉 Input: house features
  👉 Output: predicted price

---

## 📸 Output

* User inputs house details
* System predicts price using ML model

---

## 💡 Future Improvements

* Add more advanced ML models
* Deploy project on cloud
* Add authentication system

---

## 👨‍💻 Author

Vedant Suthar
Python & Odoo Developer
