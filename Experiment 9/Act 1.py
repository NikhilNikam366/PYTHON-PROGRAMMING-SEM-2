#  Use math module to calculate EMI interest
"""
Created on Mon Apr 20 09:19:47 2026

@author: Nikhil Nikam
"""

import math

def calculate_emi(principal, annual_rate, tenure_years):
   
    monthly_rate = annual_rate / (12 * 100)
    
   
    tenure_months = tenure_years * 12
    
    emi = principal * monthly_rate * math.pow(1 + monthly_rate, tenure_months) / \
          (math.pow(1 + monthly_rate, tenure_months) - 1)
    
    return emi

principal = 500000     
annual_rate = 8.5     
tenure_years = 5        

emi = calculate_emi(principal, annual_rate, tenure_years)
print(f"Monthly EMI: {emi:.2f}")
