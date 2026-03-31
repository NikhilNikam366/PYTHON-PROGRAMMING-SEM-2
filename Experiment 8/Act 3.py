# To demonstrate exception handling by handling ZeroDivisionError exceptions
"""
Created on Tue Mar 31 22:04:15 2026

@author: Nikhil Nikam
"""

try:
    total_bill = float(input("Enter total bill amount: "))
    people = int(input("Enter number of people: "))

    amount_per_person = total_bill / people

    print("Each person should pay:", amount_per_person)

except ZeroDivisionError:
    print("Error! Number of people cannot be zero.")

except ValueError:
    print("Invalid input! Please enter numeric values.")
