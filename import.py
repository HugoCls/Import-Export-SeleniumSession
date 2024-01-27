from selenium import webdriver
import time
import pickle


def import_session(driver):
    """
    Imports session data from a pickle file and applies it to the WebDriver.

    Args:
        driver (WebDriver): Instance of the WebDriver.

    Returns:
        WebDriver: Instance of the WebDriver with imported cookies and local/session storage.
    """

    # Loading session data from the pickle file
    with open('session.pkl', 'rb') as import_file:
        imported_data = pickle.load(import_file)

    # Add cookies
    for cookie in imported_data["cookies"]:
        driver.add_cookie(cookie)

    # Import local storage
    for key, value in imported_data["local_storage"].items():
        driver.execute_script(f"window.localStorage.setItem('{key}', '{value}')")

    # Import session storage
    for key, value in imported_data["session_storage"].items():
        driver.execute_script(f"window.sessionStorage.setItem('{key}', '{value}')")

    return driver


if __name__ == "__main__":
    
    driver = webdriver.Chrome()

    # Access the main page of the website before importing cookies and such
    driver.get("https://yourwebsite.com")

    driver = import_session(driver)

    # Accessing any specific page of the website or whatever you want
    driver.get("https://yourwebsite.com/YOUR_PAGE")

    # Pause to allow interaction with the page
    time.sleep(10000)