import streamlit as st
import numpy as np
import pickle

# Load the trained model


# Streamlit UI
st.title("Breast Cancer Classification")
st.write("Enter the relevant medical parameters to predict if a tumor is benign or malignant.")

# Input fields
radius_mean = st.number_input("Radius Mean", min_value=0.0, format="%.2f")
texture_mean = st.number_input("Texture Mean", min_value=0.0, format="%.2f")
perimeter_mean = st.number_input("Perimeter Mean", min_value=0.0, format="%.2f")
area_mean = st.number_input("Area Mean", min_value=0.0, format="%.2f")
smoothness_mean = st.number_input("Smoothness Mean", min_value=0.0, format="%.5f")

# Prediction button
if st.button("Predict"):
    input_data = np.array([[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean]])
    prediction = model.predict(input_data)
    result = "Malignant" if prediction[0] == 1 else "Benign"
    st.write(f"### Prediction: {result}")
