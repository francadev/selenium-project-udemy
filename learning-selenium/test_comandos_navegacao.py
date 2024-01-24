from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.saucedemo.com/v1/index.html")

# using find_element
# username = browser.find_element(By.ID, "user-name")
# username.send_keys("standard_user")
# browser.find_element(By.ID, "password").send_keys("secret_sauce")

# using find_elements
auth_fields = browser.find_elements(By.XPATH,"//*[@class='form_input']")
auth_fields[0].send_keys("standard_user")
# print("Elements found:", len(auth_fields))
# assert len(auth_fields) == 2, "O numero de elementos encontrados é diferente do esperado"

time.sleep(3)
browser.quit()
