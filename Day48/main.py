from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com.br/Electrolux-capacidade-removivel-antiaderente-transparente/dp/B0CC77KLF9/ref=sr_1_6?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3ALUWPPH4GJ6&dib=eyJ2IjoiMSJ9.-xBiWiadM29b42HZwXFqHKDsfzKggdyV1D-r2WSLznTE9nGOjMpekpRGZftI_l_Qt8QyYVKn-33Io7jOIzV9qx33Nq0gnk9-97x-mpArVo1pUqPilt6JHrlazWSqjIrgLtvSAQQV0DzkcZ0aI0enjsNCLPruQ4O-1-5d7EM67o4xrsu6O7evPW7z_wV3H6376M0pP7hKuDgbcw3P7_OUlH6SvvjuJmH1KSSnRp_wHi68XIJwD6kBc4DEz0XDB04NbX3qBjAPaQGxCLtZOU3pQp3nN3qatDHYWzOaeBTiBWw.IZemGzy3PkvgMnOVhJmlRk-Kip5o9aS_KxriAeaIy_0&dib_tag=se&keywords=rice%2Bcooker&qid=1774568136&sprefix=rice%2Bco%2Caps%2C377&sr=8-6&ufe=app_do%3Aamzn1.fos.fcd6d665-32ba-4479-9f21-b774e276a678&th=1")

# Automate the price search with selenium
price_real = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_centavos = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The price is R${price_real.text},{price_centavos.text}")

search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))
button = driver.find_element(By.ID, value="submit")
print(button)
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

bug_link = driver.find_element(By.XPATH, "xpath aqui")
print(bug_link)
# Close the page
#driver.close() # Closes the particular tab
driver.quit() # Quit the entire program