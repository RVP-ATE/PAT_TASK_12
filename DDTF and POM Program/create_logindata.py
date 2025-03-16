# Import the necessary libraries
from openpyxl import Workbook  # To work with Excel files
from datetime import datetime  # To get the current date and time

# Function to create and populate an Excel file
def create_excel_file():
    # Create a new workbook and access the active sheet
    wb = Workbook()
    ws = wb.active

    # Add column headers to the first row
    ws.append(["Test ID", "Username", "Password", "Date", "Time of Test", "Name of Tester", "Test Result"])

    # Sample data for usernames and passwords
    usernames = ["Admin", "admin123", "Admin", "Admin", "Admin"]
    passwords = ["admin123", "Tiger", "admin123", "Lion", "admin123"]

    # Loop through the usernames and passwords, adding data to the Excel file
    for i, (username, password) in enumerate(zip(usernames, passwords), start=1):
        # Add each row with Test ID (i), username, password, current date and time, and empty values for tester name and result
        ws.append([i, username, password, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%H:%M:%S'), "Name of Tester", ""])

    # Save the workbook as "login_data.xlsx"
    wb.save("login_data.xlsx")

# Call the function to create the Excel file
create_excel_file()

