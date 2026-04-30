# -*- coding: utf-8 -*-
Created on Fri May 1 01:53:36 2026
@author: NIKHIL NIKAM
import streamlit as st
st.title(" Grocery Bill Calculator")
# Initialize session state to store items
if "items" not in st.session_state:
st.session_state.items = []
# Input fields
st. subheader("Add Grocery Item")
name = st.text_input("Item Name")
price = st.number_input("Price per item ($)", min_value=0.0, step=0.1)
quantity = st.number_input("Quantity", min_value=1, step=1)
# Add item button
if st.button("Add Item"):
if name:
total_price = price * quantity
st.session_state. items .append({
"name": name,
"price": price,
"quantity": quantity,
"total": total_price
st.success(f"{name} added successfully!")
else:
st.warning("Please enter item name.")
# Display items
st. subheader(" Bill Details")
total bill = 0
if st.session_state.items:
for i, item in enumerate(st.session_state.items, 1):
  for i, item in enumerate(st.session_state.items, 1):
st.write(f"{i}. {item['name']} - ${item['price']} x {item['quantity']} = ${item['total']}")
total_bill += item["total"]

st.markdown(" --- ")
st.subheader(f" Total Bill: ${total_bill :. 2f}")
