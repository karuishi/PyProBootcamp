from selenium import webdriver
from selenium.webdriver.common.by import By
import os

ACCOUNT_EMAIL = "pedrolucas@test.com"
ACCOUNT_PASSWORD = "123456"
GYM_URL = "https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)

login_button = driver.find_element(By.ID, "submit-button")
ActionChains(driver)
# driver.quit()