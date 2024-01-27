from selenium import webdriver
import time
import pickle


def export_session(driver):
    """
    Exports session data from the WebDriver and saves it to a pickle file.

    Args:
        driver (WebDriver): Instance of the WebDriver.

    Returns:
        None
    """

    # Get cookies
    cookies = driver.get_cookies()

    # Get local storage
    keys_local_storage = driver.execute_script("return Object.keys(window.localStorage);")
    local_storage = {key: driver.execute_script(f"return window.localStorage.getItem('{key}')") for key in keys_local_storage}

    # Get session storage
    keys_session_storage = driver.execute_script("return Object.keys(window.sessionStorage);")
    session_storage = {key: driver.execute_script(f"return window.sessionStorage.getItem('{key}')") for key in keys_session_storage}

    # Export all data to a pickle file
    data_to_export = {
        "cookies": cookies,
        "local_storage": local_storage,
        "session_storage": session_storage
    }

    with open('session.pkl', 'wb') as export_file:
        pickle.dump(data_to_export, export_file)


if __name__ == "__main__":
    
    driver = webdriver.Chrome()

    driver.get("https://yourwebsite.com")

    ### DO WHAT YOU WANT BEFORE THE EXPORT ###

    export_session(driver)

    # Pause to allow interaction with the page
    time.sleep(10000)