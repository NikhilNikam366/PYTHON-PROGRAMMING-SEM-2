# Create a BMI health checker app.
Created on Fri May 1 02:00:36 2026
@author: SANKET NIKAM

import streamlit as st
st.title(" &
BMI Health Checker")
# User inputs
st.subheader("Enter Your Details")
weight = st.number_input("Enter your weight (kg)", min_value=1.0, step=0.1)
height = st.number_input("Enter your height (meters)", min_value=0.5, step=0.01)
# Calculate BMI
if st.button("Calculate BMI"):
if height > 0:
bmi = weight / (height ** 2)
st.subheader(f"Your BMI is: {bmi :. 2f}")
# BMI Category
if bmi < 18.5:
st.warning("Underweight
elif 18.5 <= bmi < 24.9:
st.success("Normal weight
elif 25 <= bmi < 29.9:
st.warning("Overweight
else:
st.error("Obese
X")

else:
st.error("Height must be greater than 0")
# BMI Chart Info
st.markdown(" --- ")
st. subheader("
BMI Categories")
