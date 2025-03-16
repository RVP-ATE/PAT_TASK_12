# Import necessary modules from Selenium for interacting with the web elements and handling exceptions
from selenium.webdriver.common.by import By  # For locating elements by different strategies
from selenium.webdriver.support.expected_conditions import alert_is_present  # To check if an alert is present
from selenium.webdriver.support.ui import WebDriverWait  # For waiting for specific conditions to be true
from selenium.webdriver.support import expected_conditions as EC  # Provides common expected conditions like visibility, presence, etc.
from selenium.common.exceptions import TimeoutException, NoSuchElementException  # To handle specific exceptions

# Define a class for the login page interactions
class LoginPage:
    # Initialize the LoginPage object with the driver and element locators
    def __init__(self, driver):
        self.driver = driver  # WebDriver instance
        # Locators for the login page elements
        self.username_field = (By.NAME, "username")  # Locator for the username field
        self.password_field = (By.NAME, "password")  # Locator for the password field
        self.login_button = (By.XPATH, "//button[@type='submit']")  # Locator for the login button
        self.profile_img = (By.XPATH, "//img[@src='/web/index.php/pim/viewPhoto/empNumber/7']")  # Locator for profile image
        self.logout_button = (By.XPATH, "//a[@href='/web/index.php/auth/logout']")  # Locator for the logout button

    # Method to log in to the application
    def login(self, username, password):
        try:
            # Wait until the username field is visible before interacting
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username_field))
            # Enter the username and password, then click the login button
            self.driver.find_element(*self.username_field).send_keys(username)
            self.driver.find_element(*self.password_field).send_keys(password)
            self.driver.find_element(*self.login_button).click()

            # Check if an alert is present (e.g., incorrect credentials or errors)
            if alert_is_present():
                alert1 = self.driver.switch_to.alert  # Switch to the alert
                print(alert1.text)  # Print the alert message
                if alert1:
                    alert1.accept()  # Accept (close) the alert

        except TimeoutException as e:
            # Handle case where elements do not appear in the expected time
            print(f"TimeoutException: Failed to find login elements within the given time. Error: {str(e)}")
            return False
        except NoSuchElementException as e:
            # Handle case where elements are not found on the page
            print(f"NoSuchElementException: One or more elements were not found. Error: {str(e)}")
            return False
        except Exception as e:
            # Catch any other unexpected errors
            print(f"Unexpected error occurred: {str(e)}")
            return False
        # Return True if login was successful
        return True

    # Method to verify if the login was successful
    def is_login_successful(self):
        try:
            # Wait for the profile image to be present, which indicates successful login
            wait_img = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//img[@src='/web/index.php/pim/viewPhoto/empNumber/7']")))
            if wait_img:
                # If the profile image is found, click it to open the dropdown menu
                self.driver.find_element(*self.profile_img).click()
                # Wait for the logout button to appear in the dropdown menu
                wait_menu = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//*[@class='oxd-dropdown-menu']")))
                if wait_menu:
                    # Click the logout button to log out
                    self.driver.find_element(*self.logout_button).click()
            return True  # Return True if login was successful
        except TimeoutException as e:
            # Handle timeout exception if login was unsuccessful
            print(f"TimeoutException: Login was unsuccessful. Error: {str(e)}")
            return False
        except NoSuchElementException as e:
            # Handle the case where elements are not found (login failure)
            print(f"NoSuchElementException: Could not find the welcome message. Error: {str(e)}")
            return False
        except Exception as e:
            # Catch any unexpected errors during the login check
            print(f"Unexpected error occurred while checking login status: {str(e)}")
            return False





