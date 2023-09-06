from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def check_website_and_copy_element(driver, website_url):
    driver.get(website_url)
    count = 0

    while True:
        try:
            danger_span = driver.find_element(By.CLASS_NAME, "tag is-danger")
            form_token_input = driver.find_element(By.ID, "form-token")
            primary_button = driver.find_element(By.CLASS_NAME, "button is-primary")

            form_token_input.clear()
            form_token_input.send_keys(danger_span.text)
            primary_button.click()

            break  # Exit the loop once the actions are done

        except NoSuchElementException:
            try:
                h1_element = driver.find_element_by_xpath("//h1[contains(text(), 'Your attendance')]")
                driver.refresh()
            except:
                pass

# Initialize the Selenium WebDriver
driver = webdriver.Chrome()  # You can use other browser drivers as well

website_url = "https://sis.galvanize.com/cohorts/64/attendance/mine/"

check_website_and_copy_element(driver, website_url)

# Close the WebDriver when done
driver.quit()
