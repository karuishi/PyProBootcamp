from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

# Selecting the first language option

# Check the right panel for upgrades and purchase de most expensive one
num_cookies = driver.find_element(By.ID, "cookies").text
#print(num_cookies)


driver.quit()