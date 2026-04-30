# Create a student result calculator app.
Created on Fri May 1 02:04:09 2026
@author: NIKHIL NIKAM

IT IT IT

import streamlit as st
st.title("Student Result Calculator")
st.subheader("Enter Marks for 5 Subjects")
# Input marks
sub1 = st.number_input("Subject 1", min_value=0, max_value=100)
sub2 = st.number_input("Subject 2", min_value=0, max_value=100)
sub3 = st.number_input("Subject 3", min_value=0, max_value=100)
sub4 = st.number_input("Subject 4", min_value=0, max_value=100)
sub5 = st.number_input("Subject 5", min_value=0, max_value=100)
# Calculate result
if st.button("Calculate Result"):
total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5
st.subheader(f" In Total Marks: {total}/500")
st. subheader(f"

Percentage: {percentage: .2f}%")
# Grade calculation
if percentage >= 90:
grade = "A+"
st.success("Grade: A+ *"
elif percentage >= 75:
grade = "A"
st.success("Grade: A
elif percentage >= 60:
grade = "B"
st.info("Grade: B
elif percentage >= 50:
