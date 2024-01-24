from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")
browser.implicitly_wait(10)

dropdown_products = Select(browser.find_element(By.XPATH, "(//*[@id='first'])[2]"))
time.sleep(2)
dropdown_products.select_by_value("Google")
time.sleep(2)

multi_value_dropdown_food = Select(browser.find_element(By.XPATH, "(//*[@id='second'])[2]"))
multi_value_dropdown_food.select_by_visible_text("Pizza")
time.sleep(2)
multi_value_dropdown_food.select_by_visible_text("Burger")
time.sleep(2)
