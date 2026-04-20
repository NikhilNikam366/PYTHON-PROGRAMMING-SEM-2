# Generate OTP using random module
"""
Created on Mon Apr 20 09:32:10 2026

@author: Nikhil Nikam
"""

import random

def generate_otp(length=6):
    otp = ""
    for _ in range(length):
        otp += str(random.randint(0, 9))
    return otp

# Example usage
otp = generate_otp()
print("Your OTP is:", otp)
