import streamlit as st
import numpy as np
import os
import joblib

model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'model.pkl')
model = joblib.load(model_path)


st.title("🔭 Gamma vs Hadron Classifier")
st.write("Enter the values for each feature below to classify the particle as Gamma or Hadron.")

#input fields for the features
features = []
feature_names = [
    "fLength", "fWidth", "fSize", "fConc", "fConc1", 
    "fAsym", "fM3Long", "fM3Trans", "fAlpha", "fDist"
]
for name in feature_names:
    value = st.number_input(f"Enter value for {name}:", value=0.0, format="%.2f")
    features.append(value)
    
#predict button
if st.button("Predict"):
    prediction = model.predict([features])[0]
    label =  "🌠 Gamma Ray" if prediction == 1 else "💥 Hadron"
    st.success(f'Prediction: {label}')   