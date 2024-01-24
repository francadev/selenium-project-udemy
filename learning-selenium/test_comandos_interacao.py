from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# access page
browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.saucedemo.com/v1/index.html")

# Chama a primeira guia de "windows_before"
window_before = browser.window_handles[0]

# find element
username = browser.find_element(By.ID, "user-name")
password = browser.find_element(By.ID, "password")
btn_login = browser.find_element(By.ID, "login-button")

# open new tab
# browser.execute_script("window.open('https://pt.stackoverflow.com/questions')")
# window_after = browser.window_handles[1]
# browser.switch_to.window(window_after)

# insert keys
username.send_keys("standard_user")
password.send_keys("secret_sauce")
btn_login.click()

# check if the next page after login has entered
product_title = browser.find_element(By.XPATH, "//*[@class='product_label']")
assert product_title.text == "Products", "Incorrect page!"

# check if the products has loaded
img_backpack = browser.find_element(By.XPATH, "(//*[@class='inventory_item_img'])[2]")
print(img_backpack.get_attribute("src"))

# quit
time.sleep(3)
browser.quit()
