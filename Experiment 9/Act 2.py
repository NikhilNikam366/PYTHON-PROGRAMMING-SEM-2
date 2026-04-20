# Display today's date in a hospital appointment system
"""
Created on Mon Apr 20 09:29:23 2026

@author: Nikhil Nikam
"""

from datetime import datetime

def get_today_date():
    today = datetime.today()
    # Format: Day Month Year (e.g., 20 April 2026)
    formatted_date = today.strftime("%d %B %Y")
    return formatted_date

def display_appointment_header():
    print("=== Hospital Appointment System ===")
    print(f"Today's Date: {get_today_date()}")
    print("----------------------------------")

# Run the function
display_appointment_header()
