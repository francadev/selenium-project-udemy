from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://demo.applitools.com/")

username = browser.find_element(By.ID, "username")
checkbox_remember_me = browser.find_element(By.XPATH, "//*[@class='form-check-input']")

assert username.is_displayed()
assert not checkbox_remember_me.is_selected()
checkbox_remember_me.click()
assert checkbox_remember_me.is_selected()
time.sleep(3)
