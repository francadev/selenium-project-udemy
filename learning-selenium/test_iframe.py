import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome()
browser.get("https://chercher.tech/practice/frames")
browser.maximize_window()
browser.implicitly_wait(10)

# access frame1
iframe1 = browser.find_element(By.ID, "frame1")
browser.switch_to.frame(iframe1)
browser.find_element(By.XPATH, "//*[@id='topic']//following-sibling::input").send_keys("iframe1")

# access frame3
iframe3 = browser.find_element(By.ID, "frame3")
browser.switch_to.frame(iframe3)
browser.find_element(By.ID, "a").click()

# back to default frame
browser.switch_to.default_content()
# access frame2
iframe2 = browser.find_element(By.ID, "frame2")
browser.switch_to.frame(iframe2)
dropdown_animals = Select(browser.find_element(By.XPATH, "//select[@id='animals']"))
dropdown_animals.select_by_value("avatar")
time.sleep(3)
