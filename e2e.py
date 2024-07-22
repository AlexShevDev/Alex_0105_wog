from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import ChromiumOptions


# Test the web service
def test_scores_service(app_url):
    chrome_options = ChromiumOptions()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(app_url)
        score_element = driver.find_element(By.XPATH, '//*[@id="score"]')

        # Check that it is a number between 1 and 1000 and return a boolean value if it’s true or not
        try:
            score_converted = int(score_element.text)
            return 1 <= score_converted <= 1000
        except ValueError:
            print("Score is not a valid integer.")
            return False

    except Exception as error:
        print(f"An error occurred: {error}")
        return False

def main_function():
    test_url = 'http://127.0.0.1:8000'
    test_passed = test_scores_service(test_url)

    if test_passed:
        return 0   # Passed
    else:
        return -1  # Didn't pass

# print(main_function())