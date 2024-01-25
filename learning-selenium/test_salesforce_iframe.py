from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(5)
browser.get(
    "https://tbid.digital.salesforce.com/oauth2/aus5v9466wdqLdY0O697/v1/authorize?response_type=code&response_mode=query&nonce=c276d232-5570-43f6-8e99-3a1e75f94ce0&client_id=0oa5v93ebgAGqkFSn697&redirect_uri=https%3A%2F%2Fiis.digital.salesforce.com%2Fservices%2Foauth2%2Fcallback&state=eyJyZWZlcnJlciI6Imh0dHBzOi8vdHJhaWxoZWFkLnNhbGVzZm9yY2UuY29tLyIsImNsaWVudElkIjoiM01WRzlnOXJic1RrS25BWFJVX2hPTHZIUllqN0hTMWNzTjBMbGhPU2VCUnY1TnAybXhQdXJjSWZmQTVWMHpuOC51SUR0Ym1YeVNXbXhxX1hkQTh3eCIsInJlZGlyZWN0VXJpIjoiaHR0cHM6Ly90cmFpbGhlYWQuc2FsZXNmb3JjZS5jb20vYXV0aC90YmlkbG9naW4vY2FsbGJhY2s_cHJvbXB0PWxvZ2luJmxvY2FsZT1wdF9CUiIsInN0YXRlIjoiNjFlMjkxMWZmYmJiMGJmMGE0NThkNjkwN2EzYTkwMjRkNjIzZDQ0MTk5OTUwOTI0IiwiY29ycmVsYXRpb25JZCI6IjA1ODk2ZjAyLTc1ZTMtNDIzZC1hNTU0LTRhY2M5OTNkMGIxOSIsInN0YXJ0VGltZSI6MTcwNjEyMDgwODU2N30&scope=openid+email+profile&intent=login")
browser.find_element(By.ID, "onetrust-accept-btn-handler").click()


def get_shadow_root(element):
    return browser.execute_script('return arguments[0].shadowRoot', element)


# Find the first shadow host element
shadow_host1 = browser.find_element(By.TAG_NAME, 'idx-standard-login-page')
root1 = get_shadow_root(shadow_host1).find_element(By.CLASS_NAME, 'login__container')

shadow_host2 = root1.find_element(By.TAG_NAME, 'lwc-idx-user-login')
root2 = get_shadow_root(shadow_host2).find_element(By.CLASS_NAME, 'idx-auth-form')

shadow_host3 = root2.find_element(By.TAG_NAME, 'lwc-wes-input')
get_shadow_root(shadow_host3).find_element(By.ID, 'field').send_keys("teste")

time.sleep(5)
