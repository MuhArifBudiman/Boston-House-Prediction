import streamlit as st
import numpy as np
import joblib

# Load model hasil tuning
model = joblib.load("xgb_best_model.pkl")

st.title("🏠 Boston House Price Prediction (XGBoost Tuned)")
st.write("Masukkan nilai fitur untuk memprediksi **MEDV (harga rumah median, $1000s)**")

# Input fitur
nox = st.number_input("NOX (Nitric Oxides Concentration)", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
lstat = st.number_input("LSTAT (% lower status population)", min_value=0.0, max_value=40.0, value=10.0, step=0.1)
rm = st.number_input("RM (Average rooms per dwelling)", min_value=1.0, max_value=10.0, value=6.0, step=0.1)
dis = st.number_input("DIS (Distance to employment centres)", min_value=1.0, max_value=15.0, value=5.0, step=0.1)
ptratio = st.number_input("PTRATIO (Pupil-teacher ratio)", min_value=10.0, max_value=30.0, value=18.0, step=0.1)
tax = st.number_input("TAX (Property tax rate)", min_value=100, max_value=800, value=300, step=1)

# Prediksi
if st.button("🔮 Predict House Price"):
    features = np.array([[nox, lstat, rm, dis, ptratio, tax]])
    prediction = model.predict(features)[0]
    st.success(f"🏡 Predicted MEDV (House Price): ${prediction*1000:.2f}")