from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

# Replace with the URL of the webpage you want to monitor
url = "https://sis.galvanize.com/cohorts/64/attendance/mine/"

# Set up the Selenium web driver (adjust the path to your driver executable)
driver = webdriver.Chrome(executable_path="path/to/chromedriver")

def find_and_click_token_button():
    try:
        button = driver.find_element_by_xpath("//button[contains(text(), 'token')]")
        button.click()
        print("Clicked the 'token' button")
    except NoSuchElementException:
        print("'token' button not found")

try:
    driver.get(url)
    while True:
        find_and_click_token_button()
        time.sleep(5)  # Adjust the interval (in seconds) between checks
except KeyboardInterrupt:
    print("Script terminated by user")
finally:
    driver.quit()
