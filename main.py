
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()


driver.get("https://www.saucedemo.com")

username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys("standard_user")  


password_field = driver.find_element(By.ID, "password")
password_field.send_keys("secret_sauce")  # Use the demo password

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

time.sleep(5)
#wait until visibility

dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))


dropdown.select_by_visible_text("Price (high to low)")




time.sleep(3)


driver.quit()

