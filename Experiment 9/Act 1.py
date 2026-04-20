# Use math module to calculate EMI interest
"""
Created on Mon Apr 20 14:53:30 2026

@author: Nikhil Nikam
"""

import math

principal = float(input("Enter the loan amount (principal): "))
annual_rate = float(input("Enter the annual interest rate (in %): "))
time_years = float(input("Enter the loan tenure (in years): "))

monthly_rate = annual_rate / (12 * 100)

months = time_years * 12

emi = (principal * monthly_rate * math.pow(1 + monthly_rate, months)) / (math.pow(1 + monthly_rate, months) - 1)

print(f"Monthly EMI is: {emi}")

total_payment = emi * months
total_interest = total_payment - principal

print(f"Total payment: {total_payment}")
print(f"Total interest payable: {total_interest}")
