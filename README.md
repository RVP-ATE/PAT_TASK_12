Automated Login Test Suite
This Python program automates login testing for a web application using Selenium WebDriver and stores test results in an Excel sheet. The program reads test data (username, password) from an Excel file, performs login actions, and writes the test results (pass/fail) along with the current date and time back to the same Excel file.

Prerequisites
Ensure that you have the following installed on your system:

Python 3.x
Selenium WebDriver
OpenPyXL
Pytest
Additionally, you will need the Chrome WebDriver for Selenium to run the tests in Google Chrome.

Install the required Python packages:
bash
Copy
pip install selenium openpyxl pytest
Setup and Usage
Clone or download this repository to your local machine.

Download ChromeDriver:

Ensure you have the correct version of ChromeDriver installed for your version of Chrome. Make sure chromedriver is in your system’s PATH or specify the full path to it in the code.
Prepare your Test Data Excel File:

Ensure the test data is stored in an Excel file named login_data.xlsx located in the same directory as the script.

The Excel file should have the following structure:

Test ID	Username	Password	...	...	Date	Time	Test Result
1	user1	pass1	...	...	...	...	
2	user2	pass2	...	...	...	...	
...	...	...	...	...	...	...	
The LoginPage Class:

The LoginPage class (assumed to be defined in LoginPage.py) is responsible for automating the login process and verifying the login success. It should have methods like:
login(username, password) – To perform login actions.
is_login_successful() – To verify if login was successful.
Running the Tests:

To run the tests, execute the script using Pytest:
bash
Copy
pytest your_script_name.py
Viewing Test Results:

After running the tests, the results will be written to the same login_data.xlsx file.
The "Test Result" column will be updated with "Test Passed" or "Test Failed".
The current date and time of the test execution will be added to the respective columns.
Code Explanation
Setup Fixture:

The setup function initializes the Selenium WebDriver (using Chrome), navigates to the login page, and maximizes the browser window. It ensures the WebDriver instance is properly set up before the test and is cleaned up after the test.
Test Data:

The read_test_data(file_path) function reads the Excel file login_data.xlsx, retrieves the necessary test data (username, password), and returns it.
Test Results:

The write_test_result(ws, row, result) function writes the test result ("Test Passed" or "Test Failed") to the Excel file, along with the current time and date of the test execution.
Test Execution:

The test_login(setup) function iterates over the test data, performs the login operation, checks if the login was successful, and writes the result back to the Excel file.
